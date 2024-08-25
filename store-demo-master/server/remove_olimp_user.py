from flask import Blueprint
from data import db_session, user_olimpyc
from flask import jsonify, request
from token_required import token_required
from sqlalchemy import insert, delete
from uuid import uuid4
import sqlalchemy

blueprint_remove_olimp_user = Blueprint('blueprint_remove_olimp_user', __name__)


@blueprint_remove_olimp_user.route('/api/remove_olimp_user', methods=['POST'])
@token_required
def remove_olimp_user(current_user):
    session = db_session.create_session()
    json_obj = request.get_json() or {}
    if json_obj.get('olimp_id', 0):
        if not session.query(user_olimpyc.Relation).filter(user_olimpyc.Relation.olimp == json_obj['olimp_id']).all():
            return jsonify({'success': 'OK', 'info': 'Уведомления уже отключены'})
        else:
            query = delete(user_olimpyc.Relation).where((user_olimpyc.Relation.olimp == json_obj['olimp_id']) & (user_olimpyc.Relation.user == current_user.id))
            session.execute(query)
            session.commit()
            return jsonify({'success': 'OK'})
    else:
        return jsonify({'success': 'there is no olimp id'})
