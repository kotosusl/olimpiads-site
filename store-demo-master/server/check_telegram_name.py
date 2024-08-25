from flask import Blueprint
from data import db_session
from flask import jsonify, request
from token_required import token_required
from data import olimpics, subjects, olimp_subject, user_olimpyc, users, user_subject, usernames_in_bot
from sqlalchemy import select


blueprint_check_telegram_name = Blueprint('blueprint_check_telegram_name', __name__)


@blueprint_check_telegram_name.route('/api/check_telegram_name', methods=['GET'])
@token_required
def check_telegram_name(current_user):
    if current_user.telegram_id:
        return jsonify({'success': 'OK', 'info': 'Username подтверждён.'})
    if not current_user.telegram_name:
        return jsonify({'success': 'OK', 'info': 'Введите Ваш username'})
    session = db_session.create_session()
    q = select(usernames_in_bot.Usernames_in_bot).select_from(usernames_in_bot.Usernames_in_bot).where(usernames_in_bot.Usernames_in_bot.telegram_username == current_user.telegram_name)
    user = list(session.execute(q))
    if len(user) == 0:
        return jsonify({'success': 'OK',
                        'info': 'Username не найден. Проверьте имя пользователя в Telegram на наличие ошибок. Перейдите в бот и нажмите "Старт".'})
    else:
        user = session.query(users.User).where(users.User.telegram_name == current_user.telegram_name).first()
        user.telegram_id = session.query(usernames_in_bot.Usernames_in_bot.user_telegram_id).where(usernames_in_bot.Usernames_in_bot.telegram_username == current_user.telegram_name).first()[0]
        session.commit()
        return jsonify({'success': 'OK', 'info': 'Username подтверждён.'})

