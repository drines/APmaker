
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.14
# REVISED DATE:     2019.05.16
# PURPOSE:  Code development & testing of the Autoprotocol library in Python.
#
# NOTES:    General notes and rules for working with Autoprotocol...
#           REFS: A ref is a short alphanumeric name given to a container
#           to identify it in later instructions. Every container referenced
#           in a protocol must also be given a destiny: either discarded at
#           the end of the protocol, or stored.
#           INSTRUCTIONS: json formatted code that creates a serial list
#           of commands to control robotic hardware execution.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python ap_maker.py --plates <csv file for plate list>
#                         --logging <log level: info, debug>
#   Example call:
#      python ap_maker.py --plates plates.csv --logging info
##

# Imports python modules
from autoprotocol.protocol import Protocol

from apm_logging import MyLogger
from input_arguments import get_input_args
from plates import Plate, read_plate_file
from generate_json import dump_json


@MyLogger
def main():
    """
    The main function for testing the json output.
    PARAMETERS: None
    RETURNS:    None
    """
    # parse in the input arguments
    in_args = get_input_args()

    # get the list of plates (assay and reagent) to be used
    plate_dict = read_plate_file(in_args.barcode_file)

    # TODO: breakout the individual actions into separate functions
    #for key in plate_dict.keys():
     #   print(plate_dict[key])

    #     # print("working on barcode: {}".format(plate_dict[key].barcode))
    #     # build_ap_obj(plate_dict[key], ap)
    #     plate_obj = Plate(key, 96, )
    #     plate_obj.plate_protocol()
    #     print(key.ap)

    # #print(ap)
    # # serialize the protocol and output to a Autoprotocol
    # # file for loading into the Tx software.
    dump_json(plate_dict)


# Call to main function to run the program
if __name__ == "__main__":
    main()
