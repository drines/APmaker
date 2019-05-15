#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.15
# REVISED DATE:     2019.05.15
# PURPOSE:  Built-in logging capabilities
#
# NOTES:    To help debug issues relating to exceptions or 
#           JSON file development, APmaker utilizes a set of
#           log files. These are stored in the log folder.
#
##

# Imports python modules
import logging
from time import time, sleep


class MyLogger:
    """
    Python decorator class for handling exception logging.
    """
    def __init__(self, function):
        """
        Creates the log file and gets a handle to the file.
        PARAMETERS: function for wrapping
        RETURNS:    fh = the instantiated file handle
        """
        # the passed in function
        self.function = function

        # instantiate the logger
        self.logger = logging.getLogger("function")
        self.logger.setLevel(logging.INFO)

        # create the file logger handle
        self.fh = logging.FileHandler("./logs/json_info_build.log")
        fmt = '%(asctime)s - %(levelname)s - %(name)s %(message)s: '
        fmt += self.function.__name__
        formatter = logging.Formatter(fmt)
        self.fh.setFormatter(formatter)

        # add handler to logger object
        self.logger.addHandler(self.fh)

    def __call__(self, *args, **kwargs):
        """
        Wraps the function with logging commands to keep the
        function calls clean and DRY.
        PARAMETERS: *args, **kwargs
        RETURNS:    result = function specific output
        """
        # code executed before wrapped function
        self.logger.info('called')

        result = self.function(*args, **kwargs)

        # code executed after wrapped function
        self.logger.info('exited')

        # finish up the wrapped function call and return any result
        return result
