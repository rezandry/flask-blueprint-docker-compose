from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from course.modules import settings

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

from course.modules.course.views import course

app.register_blueprint(course, url_prefix='/api/course')
