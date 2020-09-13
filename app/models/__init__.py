from app import db, login_manager
from app.models.auth import Auth
from app.models.storage import Storage
from log import LogConfigurator


LogConfigurator.setup_logging()
logger = LogConfigurator.get_logger(__name__)
logger.info("At Model Initialization")


def initialize_db():
    logger.info("Initializing Databases: {0} & {1}"
                .format(Auth.__name__, Storage.__name__))
    db.create_all()
    
    
@login_manager.user_loader
def load_user(user_id):
    cred = Auth.query.get(int(user_id))
    logger.info("Loading User")
    return cred


__all__ = ['Auth', 'Storage', 'initialize_db']
