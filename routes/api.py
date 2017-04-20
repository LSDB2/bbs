from models.user import User
# from models.topic import Topic
from routes import *
from utils import log
import json

# for decorators
from functools import wraps
from werkzeug.utils import secure_filename
from models.user import User
from config import user_file_director
import os


main = Blueprint('api', __name__)

Model = User


@main.route('/login', methods=['POST'])
def login():
    json = request.json()
    pass


@main.route('/register', methods=['POST'])
def register():
    json = request.json
    print('json', json)