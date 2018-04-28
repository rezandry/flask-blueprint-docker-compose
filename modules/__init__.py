from flask import Flask
from modules.homepage.views import module_homepage
from modules.forum.views import module_forum
app = Flask(__name__)
app.register_blueprint(module_homepage, url_prefix='/')
app.register_blueprint(module_homepage, url_prefix='/home')
app.register_blueprint(module_forum, url_prefix='/forum')