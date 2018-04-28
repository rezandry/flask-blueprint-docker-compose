from flask import Flask
from modules.order.views import mod_order
app = Flask(__name__)
app.register_blueprint(mod_order, url_prefix='/order')