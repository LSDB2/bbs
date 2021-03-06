from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import time
from models import db
from models.user import User
from models.node import Node
from models.topic import Topic
from models.comment import Comment


app = Flask(__name__)
db_path = 'bbs.sqlite'
manager = Manager(app)
@app.template_filter('time')
def _time(t):
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(t)
    return time.strftime(format, value)



def register_routes(app):
    # from routes.todo import main as routes_todo
    from routes.node import main as routes_node
    from routes.topic import main as routes_topic
    from routes.auth import main as routes_auth
    from routes.comment import main as routes_comment
    from routes.api import main as routes_api

    app.register_blueprint(routes_auth, url_prefix='/auth')
    app.register_blueprint(routes_node, url_prefix='/node')
    app.register_blueprint(routes_api, url_prefix='/api')
    app.register_blueprint(routes_topic)
    app.register_blueprint(routes_comment, url_prefix='/comment')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pwd@localhost/bbs'
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    print('server run')
    # app = configured_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)


def configure_manager():
    """
    这个函数用来配置命令行选项
    """
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()


