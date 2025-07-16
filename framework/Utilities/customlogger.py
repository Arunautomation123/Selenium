import logging

class LogGen:
    @staticmethod
    def logGen():
        logging.basicConfig(filename=r"D:\Users\M12378A\PycharmProjects\Selenium\framework\logs\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p', force=True, level=logging.INFO)
        logger = logging.getLogger('')
        return logger