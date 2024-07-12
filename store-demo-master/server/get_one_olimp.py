from flask import Blueprint
from data import db_session
from flask import jsonify, request
from token_required import token_required
from data import olimpics

blueprint_get_one_olimp = Blueprint('blueprint_get_one_olimp', __name__)


@blueprint_get_one_olimp.route('/api/get_one_olimp', methods=['POST'])
@token_required
def get_one_olimp(current_user):
    try:
        session = db_session.create_session()
        json_obj = request.get_json() or {}
        if json_obj.get('olimp_id', 0):
            olimp = session.query(olimpics.Olimp).filter(olimpics.Olimp.id == json_obj['olimp_id']).first()
            jsn = {
                'success': 'OK',
                'olimp': {
                    'id': olimp.id,
                    'name': olimp.name,
                    'href': olimp.href,
                    'desc': olimp.desc,
                    'min_class': olimp.min_class,
                    'max_class': olimp.max_class
                }
            }
        else:
            jsn = {'success': 'no olimp_id'}
        return jsonify(jsn)
    except Exception as err:
        return jsonify({'success': 'ERROR'})