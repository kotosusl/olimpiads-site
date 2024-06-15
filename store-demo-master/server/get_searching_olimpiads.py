from data import db_session
from flask import jsonify, request, Blueprint
from token_required import token_required
from sqlalchemy import select
from data import subjects, olimp_subject, olimpics

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
        q = q.where(olimpics.Olimp.min_class <= json_obj['search_class']).where(
            olimpics.Olimp.max_class >= json_obj['search_class'])
    search_olimps = session.execute(q)
    if json_obj.get('name_olimp', 0) and json_obj['name_olimp']:
        s = []
        for i in search_olimps:
            if json_obj['name_olimp'].lower() in i[0].name.lower():
                s.append(i[0])
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
                'id': p.id,
                'name': p.name,
                'href': p.href,
                'desc': p.desc,
                'min_class': p.min_class,
                'max_class': p.max_class
            } for p in search_olimps
        ]
    }

    return jsonify(jsn)