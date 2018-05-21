from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from order.modules import settings

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

from order.modules.order.views import order

app.register_blueprint(order, url_prefix='/api/order')
