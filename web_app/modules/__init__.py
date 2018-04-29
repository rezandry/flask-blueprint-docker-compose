from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from web_app.modules import settings

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

from web_app.modules.homepage.views import module_homepage
from web_app.modules.forum.views import module_forum
from web_app.modules.courses.views import mod_courses
from web_app.modules.blog.views import blog
from web_app.modules.order.views import mod_order

app.register_blueprint(module_homepage, url_prefix='/')
app.register_blueprint(module_homepage, url_prefix='/home')
app.register_blueprint(module_forum, url_prefix='/forum')
app.register_blueprint(mod_courses, url_prefix='/courses')
app.register_blueprint(blog, url_prefix='/blog')
app.register_blueprint(mod_order)


