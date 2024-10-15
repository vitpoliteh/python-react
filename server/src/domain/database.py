from sqlalchemy import create_engine
from config.app import app_config


engine = create_engine(app_config.db_config.db_name)
