from flask import render_template, Blueprint, jsonify
forum = Blueprint(
    'module_forum', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@forum.route('/')
def index():
    data = [
        {"id": 1, "title":"Flask vs Golang"},
        {"id": 2, "title":"Best Python framework out there?"},
        {"id": 3, "title":"What to do using python in machine learning"}
    ]
    return jsonify(data)