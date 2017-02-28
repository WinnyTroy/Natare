#!task/bin/python

from flask_script import Server, Manager, Shell
from app import create_app, db
from flask_migrate import MigrateCommand, Migrate
import os
from app.models import Users


# create the application based on the configuration in the environment
# if the configuration is not set, it will use default setting
app = create_app(os.getenv("FLASK_CONFIG") or "default")

# pass the application object to manager and create a manager instance, to enable running the application
manager = Manager(app)
migrate = Migrate(app, db, directory="migrations")

# set up a server to run at a specific port and host
server = Server(host="127.0.0.1", port=8000)


def make_shell_context():
    """
    Enables us to make a shell context within the application and run certain commands
    :return: A dictionary with the variables that will be in the shell context
    :rtype: dict
    """
    return dict(
        app=app,
        db=db,
        users=Users
    )

# add the commands that will be used in the application
# run these commands with python manage.py shell/runserver/etc...
manager.add_command("shell", Shell(make_context=make_shell_context()))
manager.add_command("runserver", server)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
