from models.node import Node
from routes import *

# for decorators
from functools import wraps


main = Blueprint('node', __name__)

Model = Node


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


@main.route('/')
def index():
    cu = current_user()
    if cu.id != 1:
        return redirect(url_for('auth.index'))
    ms = Model.query.all()
    print('所有node', ms)
    return render_template('node_index.html', node_list=ms, cu=cu)

#
# @main.route('/new')
# def new():
#     return render_template('node_new.html')


@main.route('/<int:id>')
def show(id):
    print('show node, ', id, type(id))
    m = Model.query.get(id)
    print(id, m)
    cu = current_user()
    return render_template('node.html', node=m, cu=cu)


@main.route('/edit/<id>')
def edit(id):
    t = Model.query.get(id)
    return render_template('node_edit.html', todo=t)


@main.route('/add', methods=['POST'])
def add():
    cu = current_user()
    if cu.id != 1:
        return redirect(url_for('auth.index'))
    form = request.form
    print('form', form )
    m = Model(form)
    m.save()
    print('新建的node', m)
    return redirect(url_for('.index'))


@main.route('/delete/<int:id>')
@admin_required
def delete(id):
    cu = current_user()
    if cu.id != 1:
        return redirect(url_for('auth.index'))
    t = Model.query.get(id)
    t.delete()
    return redirect(url_for('.index'))
