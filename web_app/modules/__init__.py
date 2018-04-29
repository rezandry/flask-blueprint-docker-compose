from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from web_app.modules import settings

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

from web_app.modules.homepage.views import home
from web_app.modules.forum.views import forum
from web_app.modules.course.views import course
from web_app.modules.blog.views import blog
from web_app.modules.order.views import order

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(forum)
app.register_blueprint(blog, url_prefix='/blog')
app.register_blueprint(order)
app.register_blueprint(course)
