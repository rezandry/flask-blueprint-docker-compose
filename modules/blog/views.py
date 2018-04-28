from flask import render_template, Blueprint

blog = Blueprint(
    'blog', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@blog.route('/')
def index():
    return render_template("blog.html")