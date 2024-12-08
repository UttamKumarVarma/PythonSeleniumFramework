import inspect
import logging

class BaseClass:
    def getLogger(self):
        loggerName= inspect.stack()[1][3]
       # log = logging.getLogger(__name__)  # "__name__" helps to capture the file name
        log = logging.getLogger(loggerName)  # "__name__" helps to capture the file name

        fileHandler = logging.FileHandler("output.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        log.addHandler(fileHandler)

        log.setLevel(logging.INFO)
        return log