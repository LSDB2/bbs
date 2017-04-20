from models.user import User
# from models.topic import Topic
from routes import *
from utils import log
# for decorators
from functools import wraps
from werkzeug.utils import secure_filename
from models.user import User
from config import user_file_director
import os


main = Blueprint('auth', __name__)

Model = User


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        print('admin required')
        if request.args.get('uid') != '1':
            print('not admin')
            abort(404)
        return f(*args, **kwargs)
    return function


@main.route('/logout')
def logout():
    session.pop('uid', None)
    return redirect(url_for('topic.index'))


@main.route('/')
def index():
    # ms = Model.query.all()
    return render_template('注册登录.html')


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)
    user = Model.query.filter_by(username=u.username).first()
    if u.valid_login(user):
        session.permanent = True
        session['uid'] = user.id
        print('登录成功')
        return redirect(url_for('topic.index'))
    else:
        print('登录失败')
        return render_template('注册登录.html')


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    log('u', u)
    if u.valid():
        u.save()
        print('注册成功')
    else:
        print('注册失败')
    return render_template('注册登录.html')


@main.route('/user_index')
def user_index():
    return render_template('user_index.html')


@main.route('/profile/<int:id>')
def profile(id):
    u = current_user()
    cu = Model.query.filter_by(id=id).first()
    if u.id != u.id:
        return redirect(url_for('.index'))
    else:
        return render_template('profile.html', user=cu, cu=u)


def allow_file(filename):
    suffix = filename.split('.')[-1]
    from config import accept_user_file_type
    return suffix in accept_user_file_type


@main.route('/addimg', methods=["POST"])
def add_img():
    u = current_user()

    if u is None:
        return redirect(url_for(".profile"))

    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if allow_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(user_file_director, filename))
        u.avatar = filename
        u.save()

    return redirect(url_for(".profile", id=u.id))


@main.route("/uploads/<filename>")
def uploads(filename):
    return send_from_directory(user_file_director, filename)

