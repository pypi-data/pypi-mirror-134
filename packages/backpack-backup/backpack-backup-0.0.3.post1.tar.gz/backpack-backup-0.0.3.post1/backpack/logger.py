#!/usr/bin/env python3

import logging

msg = "See the info.log file"


class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # create a file handler
        self.handler = logging.FileHandler("debug.log")
        self.handler.setLevel(logging.INFO)

        # create a logging format
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self.handler.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(self.handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg, exc_info=True)

    def critical(self, msg: str) -> None:
        self.logger.critical(msg)

    def fh_close(self) -> None:
        self.handler.close()
