from flask.json import jsonify
from flask import Blueprint

mod_courses = Blueprint(
    'courses', __name__
)


@mod_courses.route('/')
def index():
    data = [{'id': 1,
            'title': 'Introduce with design pattern', 'url': 'https://www.youtube.com/watch?v=0jjNjXcYmAU'},
            {'id': 2,
            'title': 'Composite Design Pattern', 'url': 'https://www.youtube.com/watch?v=2HUnoKyC9l0'}
            ]
    return jsonify(data)
