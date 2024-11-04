import logging

class LoggingService:
    def __init__(self, log_file: str = "app.log"):
        # Configure basic logging to the specified file
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,  # Default to INFO level
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger("LoggingService")

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)
