from flask import Flask
from core import settings
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

# Set Settings
Settings = settings.Development


task = Flask(
    import_name=Settings.APPLICATION_NAME,
    root_path=Settings.APPLICATION_ROOT,
    template_folder=Settings.APPLICATION_TEMPLATE,
    static_folder=Settings.APPLICATION_STATIC
)

task.config.from_object(Settings)


# Add extensions into application
db = SQLAlchemy(task)
migrate = Migrate(task, db)

manager = Manager(task)
manager.add_command('db', MigrateCommand)


# init app
db.init_app(task)


# Model
class Rates(db.Model):
    __tablename__ = 'Rates'

    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.Integer())
    count_rate = db.Column(db.Integer())

    def __init__(self, rate=None, count_rate=None):
        self.rate = rate
        self.count_rate = count_rate
