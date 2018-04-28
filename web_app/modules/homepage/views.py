from flask import render_template, Blueprint
home = Blueprint(
    'module_homepage', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@home.route('/')
def index():
    return render_template('homepage.html')