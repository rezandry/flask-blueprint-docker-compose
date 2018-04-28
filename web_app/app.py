import os,sys
sys.path.append(os.path.join(os.getcwd(), 'web_app'))

from web_app.modules import app

def run_app():
    return app