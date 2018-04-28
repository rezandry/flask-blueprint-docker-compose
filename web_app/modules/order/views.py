from flask import render_template, Blueprint, jsonify

order = Blueprint(
    'order', #name of module
    __name__,
    template_folder='templates' # templates folder
)

@order.route('/')
def index():
    data = [{'id': 1, 'title': 'order from email'},{'id': 2, 'title': 'order from facebook'}]
    return jsonify(data)
