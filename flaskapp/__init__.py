from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flaskapp.user import api_blueprint as userbp
from flaskapp.common.routes import api as commonbp
app.register_blueprint(userbp, url_prefix='/users')
app.register_blueprint(commonbp, url_prefix='/common')