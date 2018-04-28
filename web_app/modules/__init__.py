from flask import Flask
from web_app.modules.homepage.views import home
from web_app.modules.forum.views import forum
from web_app.modules.courses.views import course
from web_app.modules.blog.views import blog
from web_app.modules.order.views import order

app = Flask(__name__)
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(forum, url_prefix='/forum')
app.register_blueprint(blog, url_prefix='/blog')
app.register_blueprint(order, url_prefix='/order')
app.register_blueprint(course)
