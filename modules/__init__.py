from flask import Flask
from modules.blog.views import blog


app = Flask(__name__)
app.register_blueprint(blog, url_prefix='/blog')