from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import create_app
from config import DevConfig

app = create_app(DevConfig)

manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()