from rvr_base import mylogger
from rvr_base import config
import logging
from rvr_base import constants

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
thelogger = mylogger.Mylogger()

config = config.config(constants.CONFIG_FILE)

print(config.q1('workspace_id'))