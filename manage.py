#! /usr/local/bin/python3

import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import make_response

from src.main.api import create_app, db
from src.main.api.model import User

app = create_app(os.getenv("STARTER_ENV") or "dev")
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db, directory="migrations")

with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

manager.add_command('db', MigrateCommand)

static_folder_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build")
app.static_folder = static_folder_root

app.static_url_path = "/static/"
app.url_map.strict_slashes = False


@manager.command
def run(port=5000):
    app.run(port=port, debug=True)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('src/test/pytest/', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
