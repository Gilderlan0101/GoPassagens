from flask import session


def is_user_logged_in():
    return 'user' in session
