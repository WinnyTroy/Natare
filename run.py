#!task/bin/python

from app import app, manager
from flask_migrate import MigrateCommand

app.config.from_object(__name__)

manager.add_command('db', MigrateCommand)

manager.run()

app.run(debug=True, host='0.0.0.0', port=8000)
