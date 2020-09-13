from app import app as application
from app.log.log_configurator import LogConfigurator


LogConfigurator.setup_logging()
logger = LogConfigurator.get_logger(__name__)
logger.info("Server Started")
application.run(host="0.0.0.0", port=5000)
