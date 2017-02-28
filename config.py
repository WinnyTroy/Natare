import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Configuration class for
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CSRF_ENABLE = True
    CSRF_SESSION_KEY = os.environ.get("CSRF_SESSION_KEY")
    DEBUG = False
    CSRF_ENABLED = True
    THREADS_PER_PAGE = 2
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"] or 'sqlite:///' + os.path.join(basedir, 'natare.db')
    SECURITY_PASSWORD_SALT = os.environ["SECURITY_PASSWORD_SALT"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """
    Testing configurations
    :cvar DEBUG, set to true to allow for running tests and logging
    :cvar TESTING, set to True to allow for running tests
    :cvar WTF_CSRF_ENABLED, this is for forms and is set to FALSE, in order to allow for tests
    :cvar PRESERVE_CONTEXT_ON_EXCEPTION, Enables this app to keep running in the same context even on
     occurence of an error
    :cvar SQLALCHEMY_DATABASE_URI, the db uri that will be used for testing, this will not touch the
    production db, and is faster when it comes to running tests as it is an in memory db
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class DevelopmentConfig(Config):
    """
    Configurations for production environment
    We set the DEBUG value to True, to enable logging and also run tests
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configuration that will run when the application is in production

    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')


# configuration dictionary that will be imported in other parts of the application and will be used to
# set up the app under different conditions, testing, development, production..etc
# the default configuration will be development configuration, this is in case, we forget to set one
config = {
    "testing": TestingConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
