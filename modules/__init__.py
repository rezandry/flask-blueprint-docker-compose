from flask import Flask
from modules.courses.views import mod_courses

app = Flask(__name__)
app.register_blueprint(mod_courses, url_prefix='/courses')
