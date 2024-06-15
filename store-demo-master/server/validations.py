def valid_password(password):
    if len(password) < 5:
        return 'short length password'
    if len(password) > 50:
        return 'too long password'
    return 'OK'


def valid_email(email):
    if len(email) < 5:
        return 'short length email'
    if len(email) > 50:
        return 'too long email'
    if '@' not in email or '.' not in email:
        return 'invalid email format'
    return 'OK'


def valid_school_class(school_class):
    if not school_class.isdigit():
        return 'school class is not digit'
    return 'OK'


def valid_telegram_name(telegram_name):
    if len(telegram_name) == 1:
        return 'invalid telegram name'
    if len(telegram_name) > 50:
        return 'too long telegram name'
    if telegram_name[0] != '@':
        return 'the first element is not @'
    return 'OK'