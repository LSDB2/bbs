from . import ModelMixin
from . import db
from . import timestamp


class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    ct = db.Column(db.Integer)

    #
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.ct = int(timestamp())

    def user(self):
        from models.user import User
        u = User.query.filter_by(id=self.user_id)
        return u

    def topic(self):
        from models.topic import Topic
        t = Topic.query.filter_by(id=self.topic_id)
        return t
