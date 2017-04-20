from models.topic import Topic
from models.node import Node
from routes import *


main = Blueprint('topic', __name__)

Model = Topic


@main.route('/')
def index():
    arg = int(request.args.get('node_id', -1))
    ns = Node.query.all()
    if arg == -1:
        ms = Model.query.all()
    else:
        ms = Model.query.filter_by(node_id=arg).all()
    u = current_user()
    print('u', u)
    if u is None:
        return render_template('topic/index.html', topic_list=ms, node_list=ns)
    else:
        return render_template('topic/has_login.html', topic_list=ms, node_list=ns, cu=u)


@main.route('/new')
@login_required
def new():
    print('发表新的')
    n = Node.query.all()
    print('所有node', n)
    return render_template('topic/new.html', node_list=n)


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    cu = current_user()
    m.view += 1
    m.save()
    print('m', m.comments)
    return render_template('topic/detail.html', topic=m, cu=cu)


@main.route('/edit/<id>')
def edit(id):
    cu = current_user()
    if cu is None:
        abort(404)
    t = Model.query.filter_by(id=id).first()
    return render_template('topic_edit.html', topic=t, cu=cu)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.node_id = int(form.get('node_id'))
    m.user_id = int(session['uid'])
    m.save()
    return redirect(url_for('node.show', id=m.node_id))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    m = Model.query.get(id)
    value = m.content
    m.content = form.get('content', value)
    m.save()
    return redirect(url_for('.index'))


@main.route('/delete/<int:id>')
def delete(id):
    cu = current_user()
    if cu is None:
        abort(404)
    t = Model.query.get(id)
    t.delete()
    u_id = current_user().id
    return redirect(url_for('auth.profile', id=u_id))
