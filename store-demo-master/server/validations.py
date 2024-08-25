def valid_password(password):
    if len(password) < 5:
        return 'Пароль слишком короткий'
    if len(password) > 50:
        return 'Пароль слишком длинный'
    return 'OK'


def valid_email(email):
    if len(email) < 5:
        return 'Email слишком короткий'
    if len(email) > 50:
        return 'Email слишком длинный'
    if '@' not in email or '.' not in email:
        return 'Email не соответствует формату'
    return 'OK'


def valid_school_class(school_class):
    if not school_class.isdigit():
        return 'Класс не является числом'
    return 'OK'


def valid_telegram_name(telegram_name):
    if len(telegram_name) == 1:
        return 'Неверный username в Telegram'
    if len(telegram_name) > 50:
        return 'Username слишком длинный'
    return 'OK'