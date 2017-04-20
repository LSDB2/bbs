from . import ModelMixin
from . import db
from . import timestamp


class Topic(db.Model, ModelMixin):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    ct = db.Column(db.Integer)
    view = db.Column(db.Integer)
    # has relationship with comments
    comments = db.relationship('Comment', backref="topic")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.ct = int(timestamp())
        self.view = 0

    def user(self):
        from models.user import User
        u = User.query.filter_by(id=self.user_id)
        return u

