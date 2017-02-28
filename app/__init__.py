from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    """
    Application factory, this will allow creation of multiple applications under different configurations
    :param config_name: the configuration to
    :return: a new WSGI flask application
    :rtype: object
    """
    app = Flask(__name__, template_folder="templates", static_folder="static")
    # app configurations, considering config is a dictionary, we pass in the key that we will receive
    app.config.from_object(config[config_name])

    # initialize the db
    db.init_app(app)

    # register error pages and blueprints
    # error_handlers(app)
    register_blueprints(app)

    # finally return the new flask application
    return app


# todo: implement your error handlers here
# def error_handlers(app):
#     """
#     Function that will handle the erros encountered in the application
#     :param app: Application object
#     """
#
#     # Error handler for page not found
#     @app.errorhandler(404)
#     def not_found():
#         return render_template('errorpages/404.html')
#
#     @app.errorhandler(403)
#     def error_403():
#         return render_template("errorpages/403.html")
#
#     @app.errorhandler(403)
#     def error_500():
#         return render_template("errorpages/500.html")
#
#     @app.errorhandler(400)
#     def not_found():
#         return render_template('errorpages/400.html')


def register_blueprints(app):
    """
    Register your blueprints here.
    :param app: application object
    """
    from app.mod_home import home
    from app.mod_gallery import gallery
    from app.mod_offers import offers

    app.register_blueprint(offers)
    app.register_blueprint(gallery)
    app.register_blueprint(home)
