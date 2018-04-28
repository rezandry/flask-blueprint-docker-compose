from flask import render_template, Blueprint
module_homepage = Blueprint(
    'module_homepage', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@module_homepage.route('/')
def index():
    return render_template('homepage.html')