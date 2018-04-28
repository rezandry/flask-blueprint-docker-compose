from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask.ext.jsontools import DynamicJSONEncoder
from modules import settings
from flask.ext.jsontools import JsonSerializableBase


app = Flask(__name__)
app.json_encoder = DynamicJSONEncoder
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

Base = declarative_base(cls=(JsonSerializableBase,))
Base.query = db.session.query_property()

from modules.homepage.views import module_homepage
from modules.forum.views import module_forum
from modules.courses.views import mod_courses
from modules.blog.views import blog
from modules.order.views import mod_order



app.register_blueprint(module_homepage, url_prefix='/')
app.register_blueprint(module_homepage, url_prefix='/home')
app.register_blueprint(module_forum, url_prefix='/forum')
app.register_blueprint(mod_courses, url_prefix='/courses')
app.register_blueprint(blog, url_prefix='/blog')
# app.register_blueprint(mod_order, url_prefix='/order')

app.register_blueprint(mod_order)

