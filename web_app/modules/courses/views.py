from flask.json import jsonify
from flask import Blueprint
from flask_restful import Api, Resource
from web_app.modules.courses.model import Courses


def __init__(self):
    self.model = Courses()


course = Blueprint(
    'course', __name__
)
api = Api(course)


class GetCourse(Resource):
    def get(self):
        data = [{'id': 1,
                 'title': 'Introduce with design pattern', 'url': 'https://www.youtube.com/watch?v=0jjNjXcYmAU'},
                {'id': 2,
                 'title': 'Composite Design Pattern', 'url': 'https://www.youtube.com/watch?v=2HUnoKyC9l0'}
                ]
        return jsonify(data)


api.add_resource(GetCourse, '/api/course')
