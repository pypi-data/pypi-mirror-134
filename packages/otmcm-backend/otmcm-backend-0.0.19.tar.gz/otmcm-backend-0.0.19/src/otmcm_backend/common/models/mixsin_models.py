import logging

class MixsinLogger:

    LOGGER_LOG_MSG_TEMPLATE = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    logger: logging.Logger
    
    @classmethod
    def get_logger(cls, log_level:int, logger_name:str)->logging.Logger:
        """This function define and return a logger

        Args:
            log_level (int): ex logging.WARNING

        Returns:
            logging.Logger: [description]
        """
        logger = logging.getLogger(name=logger_name)
        handler = logging.StreamHandler()
        rmatter = logging.Formatter(cls.LOGGER_LOG_MSG_TEMPLATE)
        handler.setFormatter(rmatter)
        logger.addHandler(handler)
        logger.setLevel(log_level)
        return logger


    def set_up_logger(self, log_level:int, logger_name:str=None):
        """If you want to set up an internal logger attribute, call this function

        Args:
            log_level (int): ex logging.WARNING
        """
        self.logger = self.get_logger(
            log_level=log_level,
            logger_name=f"[{self.__class__.__name__}]" if logger_name is None else logger_name
        )
    
