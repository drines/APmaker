#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.15
# REVISED DATE:     2019.05.15
# PURPOSE:   Takes in any command line arguments
#
# NOTES:     Parses and check the different command
#            line options included at program start.
##

# Imports python modules
import argparse
from apm_logging import MyLogger


@MyLogger
def get_input_args():
    """
    Retrieves and parses the command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module to created and defined these command line arguments. If
    the user fails to provide some or all of the arguments, then the default
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Barcode file as --default value 'sample_data/barcodes.xlsx'
      3. Logging level --default value 'info'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - using argparse module to store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser(description='Creates an autoprotocol ' +
                                     'JSON file including the barcoded ' +
                                     'plates file.')
    # Create the command line arguments as mentioned above
    parser.add_argument('--barcode_file',
                        type=str,
                        default='.\sample_data\\assay_plates.xlsx',
                        help='directory and file name for barcodes ' +
                        '(default: \'sample_data\\assay_plates.xlsx\'.')
    parser.add_argument('--logging',
                        type=str,
                        default='info',
                        help='log level used during program operation ' +
                        '(default: info).')

    # Return the parsed arguments back to the calling function
    return parser.parse_args()
