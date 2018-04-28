from flask import Flask
from modules.homepage.views import module_homepage
app = Flask(__name__)
app.register_blueprint(module_homepage, url_prefix='/')
app.register_blueprint(module_homepage, url_prefix='/home')