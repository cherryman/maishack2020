from flask import Flask

UPLOAD_FOLDER = 'app/static'
SECRET_KEY = 'potato'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes