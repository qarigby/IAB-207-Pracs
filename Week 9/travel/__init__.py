from flask import Flask
from flask_bootstrap import Bootstrap5

def create_app():
    app = Flask(__name__)

    # Use this to display forms quickly
    Bootstrap5(app)

    app.secret_key = 'asecretkey'
    
    #add Blueprints
    from . import views, destinations, auth
    app.register_blueprint(views.mainbp)
    app.register_blueprint(destinations.destbp)
    app.register_blueprint(auth.authbp)

    return app

