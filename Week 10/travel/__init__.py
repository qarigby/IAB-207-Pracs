from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Use this to display forms quickly
    Bootstrap5(app)

    app.secret_key = 'asecretkey'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traveldb.sqlite'
    db.init_app(app)
    
    #add Blueprints
    from . import views, destinations, auth
    app.register_blueprint(views.mainbp)
    app.register_blueprint(destinations.destbp)
    app.register_blueprint(auth.authbp)

    return app

