from data import db_session
from flask import jsonify, request, Blueprint
from token_required import token_required
from sqlalchemy import select
from data import subjects, olimp_subject, olimpics, user_olimpyc

blueprint_get_searching_olimpiads = Blueprint('blueprint_get_searching_olimpiads', __name__)


@blueprint_get_searching_olimpiads.route('/api/get_searching_olimpiads', methods=['POST'])
@token_required
def get_searching_olimpiads(current_user):
    session = db_session.create_session()
    json_obj = request.get_json() or {}
    q = select(olimpics.Olimp).select_from(olimpics.Olimp)
    if json_obj.get('subjects', 0):
        q = q.join(olimp_subject.Olimp_Subject,
                   olimpics.Olimp.id == olimp_subject.Olimp_Subject.olimp).join(subjects.Subject,
                                                                                subjects.Subject.id == olimp_subject.Olimp_Subject.subject).where(
            subjects.Subject.name.in_(json_obj['subjects']))
    if json_obj.get('search_class', 0):
        q = q.where(olimpics.Olimp.min_class <= int(json_obj['search_class'])).where(
            olimpics.Olimp.max_class >= int(json_obj['search_class']))
    q = q.limit(50)
    search_olimps = session.execute(q)
    if json_obj.get('name_olimp', 0) and json_obj['name_olimp']:
        s = []
        for i in search_olimps:
            if json_obj['name_olimp'].lower() in i[0].name.lower():
                s.append(i)
        search_olimps = s.copy()
    """
    if json_obj.get('subjects', 0):
        ids_search_subjects = [p[0] for p in session.query(subjects.Subject.id).filter(subjects.Subject.name.in_(json_obj['subjects'])).all()]
        ids_search_olimps = [p[0] for p in session.query(olimp_subject.Olimp_Subject.olimp).filter(olimp_subject.Olimp_Subject.subject.in_(ids_search_subjects)).all()]
        search_olimps = session.query(olimpics.Olimp.name).filter(olimpics.Olimp.id.in_(ids_search_olimps)).all()
    else:
        search_olimps = session.query(olimpics.Olimp).all()

    if json_obj.get('search_class', 0):
        search_olimps = session.query(olimpics.Olimp).filter(olimpics.Olimp.in_(search_olimps) & olimpics.Olimp.min_class <= json_obj['search_class'] & olimpics.Olimp.max_class >= json_obj['search_class']).all()
    """


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
                    olimp_subject.Olimp_Subject.subject == subjects.Subject.id).join(olimpics.Olimp,
                    olimpics.Olimp.id == olimp_subject.Olimp_Subject.olimp).where(olimpics.Olimp.id == p[0].id)
                ))],
                'user_have': ('True' if list(session.execute(select(user_olimpyc.Relation).select_from(user_olimpyc.Relation).where(
                    (user_olimpyc.Relation.user == current_user.id) & (user_olimpyc.Relation.olimp == p[0].id)
                ))) else 'False')
            } for p in list(search_olimps)
        ]
    }

    return jsonify(jsn)