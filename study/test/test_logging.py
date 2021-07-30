import logging


class Log:
    def my_log(self, level, msg):
        logger = logging.getLogger("test.log")
        logger.setLevel("DEBUG")
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")
        fh = logging.FileHandler("test.log", encoding="utf-8")
        fh.setLevel("DEBUG")
        logger.addHandler(ch)
        logger.addHandler(fh)

        if level == "DEBUG":
            logging.debug(msg)
        elif level == "INFO":
            logging.info(msg)
        elif level == "ERROR":
            logging.error(msg)
        elif level == "WARNING":
            logging.warning(msg)
        elif level == "CRITICAL":
            logging.critical(msg)

    def getdebug(self, msg):
        Log().my_log("DEBUG", msg)

    def getinfo(self, msg):
        Log().my_log("INFO", msg)

    def geterror(self, msg):
        Log().my_log("ERROR", msg)

    def getwarning(self, msg):
        Log().my_log("WARNING", msg)

    def getcritical(self, msg):
        Log().my_log("CRITICAL", msg)


if __name__ == '__main__':
    my_logger = Log()
    my_logger.my_log("WARNING", "这是一个warning信息1")
    my_logger.getwarning("这是一个warning信息2")
