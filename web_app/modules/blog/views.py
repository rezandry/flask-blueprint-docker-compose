from flask import render_template, Blueprint, jsonify

blog = Blueprint(
    'blog', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@blog.route('/')
def index():
    data = [{'id': 1, 'title': 'Blog title 1'}, {'id': 2, 'title': 'Blog title 2'}]
    return jsonify(data)