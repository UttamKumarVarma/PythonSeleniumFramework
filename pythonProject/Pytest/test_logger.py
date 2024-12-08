import logging


def test_logging():
    log = logging.getLogger(__name__)  # "__name__" helps to capture the file name

    fileHandler = logging.FileHandler("output.log")
    formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s: %(message)s")
    fileHandler.setFormatter(formatter)
    log.addHandler(fileHandler)

    log.setLevel(logging.INFO)
    log.debug("debug statement is executed")
    log.info("info statement is executed")
    log.error("error statement is executed")
    log.warning("warning statement is executed")
    log.critical("critical message")