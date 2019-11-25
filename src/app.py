from flask import Flask

from .config import app_config
from .models import db, bcrypt
from .models import PlayerModel

def create_app(env_name):
  """
  Create app
  """

  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  bcrypt.init_app(app)

  db.init_app(app)

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your first endpoint is workin'

  return app
