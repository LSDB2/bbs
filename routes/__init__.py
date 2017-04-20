from flask import Blueprint
from flask import jsonify
from flask import redirect
from functools import wraps
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask import abort


def current_user():
    from models.user import User
    id = session.get('uid', None)
    if id is None:
        u = None
    else:
        u = User.query.filter_by(id=id).first()
    return u


def login_required(route_function):
    def func():
        u = current_user()
        print('u', u)
        if u is None:
            return redirect(url_for('auth.index'))
        return route_function()
    return func


# def login_required(f):
#     @wraps(f)
#     def function(*args, **kwargs):
#         u = current_user()
#         if u is None:
#             # print('U IS NONE')
#             return redirect(url_for('auth.index'))
#         # print('U IS NOT NONE', args, kwargs)
#         return f(*args, **kwargs)
#     return function


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        # print('admin required')
        if request.args.get('uid') != '1':
            print('not admin')
            abort(404)
        return f(*args, **kwargs)
    return function
