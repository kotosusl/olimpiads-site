from flask import Blueprint
from data import db_session
from flask import jsonify, request
from token_required import token_required
from data import olimpics, subjects, olimp_subject, user_olimpyc
from sqlalchemy import select

blueprint_get_one_olimp = Blueprint('blueprint_get_one_olimp', __name__)


@blueprint_get_one_olimp.route('/api/get_one_olimp', methods=['POST'])
@token_required
def get_one_olimp(current_user):
    try:
        session = db_session.create_session()
        json_obj = request.get_json() or {}
        if json_obj.get('olimp_id', 0):
            olimp = session.query(olimpics.Olimp).filter(olimpics.Olimp.id == json_obj['olimp_id']).first()
            q = select(subjects.Subject.name).select_from(subjects.Subject).join(olimp_subject.Olimp_Subject,
            olimp_subject.Olimp_Subject.subject == subjects.Subject.id).join(olimpics.Olimp, olimp_subject.Olimp_Subject.olimp == olimpics.Olimp.id).where(olimp.id == olimpics.Olimp.id)
            olimp_subjects = session.execute(q)
            q = select(user_olimpyc.Relation).select_from(user_olimpyc.Relation).where(
                (user_olimpyc.Relation.user == current_user.id) & (user_olimpyc.Relation.olimp == olimp.id))
            user_have = session.execute(q)
            jsn = {
                'success': 'OK',
                'olimp': {
                    'id': olimp.id,
                    'name': olimp.name,
                    'href': olimp.href,
                    'desc': olimp.desc,
                    'min_class': olimp.min_class,
                    'max_class': olimp.max_class,
                    'subjects': [p[0] for p in olimp_subjects],
                    'user_have': ("True" if list(user_have) else "False")
                }
            }
        else:
            jsn = {'success': 'no olimp_id'}
        return jsonify(jsn)
    except Exception as err:
        return jsonify({'success': 'ERROR'})