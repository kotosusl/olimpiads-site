from flask import Blueprint
from data import db_session, user_olimpyc
from flask import jsonify, request
from token_required import token_required
from sqlalchemy import insert
from uuid import uuid4


blueprint_add_olimp_to_user = Blueprint('blueprint_add_olimp_to_user', __name__)


@blueprint_add_olimp_to_user.route('/api/add_olimp_to_user', methods=['POST'])
@token_required
def add_olimp_to_user(current_user):
    session = db_session.create_session()
    json_obj = request.get_json() or {}
    if json_obj.get('olimp_id', 0):
        if session.query(user_olimpyc.Relation).filter((user_olimpyc.Relation.olimp == json_obj['olimp_id']) & (user_olimpyc.Relation.user == current_user.id)).all():
            session.close()
            return jsonify({'success': 'OK', 'info': 'Уведомления уже добавлены'})
        else:
            query = insert(user_olimpyc.Relation).values(id=str(uuid4()), user=current_user.id, olimp=json_obj['olimp_id'])
            session.execute(query)
            session.commit()
            session.close()
            return jsonify({'success': 'OK'})
    else:
        session.close()
        return jsonify({'success': 'there is no olimp id'})
