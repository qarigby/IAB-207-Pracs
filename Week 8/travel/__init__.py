from flask import Flask

def create_app():
    app = Flask(__name__)
    
    #add Blueprints
    from . import views, destinations
    app.register_blueprint(views.mainbp)
    app.register_blueprint(destinations.destbp)

    return app

