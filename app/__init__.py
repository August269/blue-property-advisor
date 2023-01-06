from flask import Flask
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    from .main import main as mainbp
    app.register_blueprint(mainbp)
    return app