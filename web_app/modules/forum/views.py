from web_app.modules.forum.model import Forum,forum_schema,forums_schema
from flask import Blueprint, jsonify, json
from flask_restful import Api, Resource


forum = Blueprint(
    'forum', #name of module
    __name__,
    template_folder='templates' # templates folder
)
api = Api(forum)

class ForumApi(Resource):
    def get(self):
        data = Forum.query.all()
        result = forums_schema.dump(data)
        return jsonify({'forums': result.data})

api.add_resource(ForumApi,'/forum/')
