import logging

class Logg():
    def __init__(self, name = __name__):
        print("logger")
        self.logger = logging.getLogger(name)
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s - %(message)s', 
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(name)
            ]
            )
        
    def info(self, message):
        print("logger", self.logger)
        self.logger.info(message)