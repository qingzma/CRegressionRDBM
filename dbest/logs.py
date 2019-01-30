#!/usr/bin/env python
# coding=utf-8
# import os, sys
# script_path=os.path.dirname(__file__)
# root_path=os.path.dirname(script_path)
# sys.path.append(root_path)

import logging.config
import logging

import os.path
default_logger_name = "../results/deletable.log"


class QueryLogs:
    """docstring for ClassName"""

    def __init__(self, log=None):
        self.fh = None  # logger file handler
        self.ch = None  # logger console handler
        self.num_dataset = 8
        self.logger = logging.getLogger(default_logger_name)
        self.logging = logging
        if log == None:
            self.set_logging(default_logger_name)
            self.logger_name = default_logger_name
        else:
            self.set_logging(log)
            self.logger_name = log
        # self.set_no_output()

    def set_logging(self, file_name=default_logger_name):
        self.logger.removeHandler(self.fh)
        self.logger.removeHandler(self.ch)
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        self.fh = logging.FileHandler(file_name, mode='w')
        self.fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        # create formatter and add it to the handlers
        formatter = self.logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        #formatter = self.logging.Formatter('%(levelname)s - %(message)s')
        #formatter = self.logging.Formatter('%(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def set_no_output(self):
        self.logger.removeHandler(self.fh)
        self.logger.removeHandler(self.ch)
        self.logger.setLevel(60)
    def set_level(self, level=logging.INFO):
        """Summary

        Args:
            level (TYPE, optional): "DEBUG", "INFO", "WARNING", "ERROR","CRITICAL"
        """
        if level is "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        if level is "INFO":
            self.logger.setLevel(logging.INFO)
        if level is "WARNING":
            self.logger.setLevel(logging.WARNING)
        if level is "ERROR":
            self.logger.setLevel(logging.ERROR)
        if level is "CRITICAL":
            self.logger.setLevel(logging.CRITICAL)


if __name__ == "__main__":
    # import dbest.qreg
    # ql = QueryLogs()
    # coreQ = dbest.qreg.CRegression()
    print(os.path.abspath(os.path.join('.', os.pardir))+'/results/deletable.log')
