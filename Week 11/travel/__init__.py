from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import datetime

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Use this to display forms quickly
    Bootstrap5(app)

    app.secret_key = 'asecretkey'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traveldb.sqlite'
    db.init_app(app)

    # Authentication setup
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    # create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.scalar(db.select(User).where(User.id==user_id))
    
    #add Blueprints
    from . import views, destinations, auth
    app.register_blueprint(views.mainbp)
    app.register_blueprint(destinations.destbp)
    app.register_blueprint(auth.authbp)

    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html", error=e)

    # this creates a dictionary of variables that are available
    # to all html templates
    @app.context_processor
    def get_context():
      year = datetime.datetime.today().year
      return dict(year=year)

    return app

