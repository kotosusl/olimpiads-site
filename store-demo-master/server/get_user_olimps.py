from data import db_session
from flask import jsonify, request, Blueprint
from token_required import token_required
from sqlalchemy import select
from data import subjects, olimp_subject, olimpics, user_olimpyc, users

blueprint_get_user_olimps = Blueprint('blueprint_get_user_olimps', __name__)


@blueprint_get_user_olimps.route('/api/get_user_olimps', methods=['POST'])
@token_required
def get_user_olimps(current_user):
    session = db_session.create_session()
    json_obj = request.get_json() or {}
    query = select(olimpics.Olimp).select_from(olimpics.Olimp).join(user_olimpyc.Relation,
            user_olimpyc.Relation.olimp == olimpics.Olimp.id).join(users.User,
            users.User.id == user_olimpyc.Relation.user).where(users.User.id == current_user.id)
    selection_olimps = session.execute(query)
    if json_obj.get('search_name', 0):
        s = []
        for i in selection_olimps:
            if json_obj['search_name'].lower() in i[0].name.lower():
                s.append(i)
        selection_olimps = s.copy()


    jsn = {
        'success': 'OK',
        'olimps': [
            {
                'id': p[0].id,
                'name': p[0].name,
                'href': p[0].href,
                'desc': p[0].desc,
                'min_class': p[0].min_class,
                'max_class': p[0].max_class,
                'subjects': [k[0].name for k in list(session.execute(
                    select(subjects.Subject).select_from(subjects.Subject).join(olimp_subject.Olimp_Subject,
                                                                                olimp_subject.Olimp_Subject.subject == subjects.Subject.id).join(
                        olimpics.Olimp,
                        olimpics.Olimp.id == olimp_subject.Olimp_Subject.olimp).where(olimpics.Olimp.id == p[0].id)
                ))],
                'user_have': ('True' if list(
                    session.execute(select(user_olimpyc.Relation).select_from(user_olimpyc.Relation).where(
                        (user_olimpyc.Relation.user == current_user.id) & (user_olimpyc.Relation.olimp == p[0].id)
                    ))) else 'False')
            } for p in list(selection_olimps)
        ]
    }

    return jsonify(jsn)

