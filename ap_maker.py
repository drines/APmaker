
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.14
# REVISED DATE:     2019.05.15
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
import json
from autoprotocol.protocol import Protocol

from apm_logging import MyLogger
from input_arguments import get_input_args


@MyLogger
def main():
    """
    The main function for testing the json output.
    PARAMETERS: None
    RETURNS:    None
    """

    # instantiate the Protocol object
    p = Protocol()

    # TODO: breakout the individual actions into separate functions

    # define the REFS section of the json output and specify
    # the current plate to use - can come from a database
    barcode = "A00001"
    current_plate = p.ref("assay_plate_1",
                          id=barcode,
                          cont_type="96-pcr",
                          storage=None,
                          discard=True)

    # weigh the mass of the plate before dispensing
    p.measure_mass(current_plate, barcode + "_mass_before")

    # fill the plate with water
    p.dispense_full_plate(current_plate, "water", "100:microliter")

    # spin the plate
    p.spin(current_plate, "1000:g", "10:minute", flow_direction="outward")

    # re-weigh the mass of the plate after dispensing
    p.measure_mass(current_plate, barcode + "_mass_after")

    # seal the plate
    p.seal(current_plate, mode="thermal", temperature="160:celsius")

    # serialize the protocol as Autoprotocol JSON
    print(json.dumps(p.as_dict(), indent=2))


# Call to main function to run the program
if __name__ == "__main__":
    main()
