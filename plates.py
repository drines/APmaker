#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.15
# REVISED DATE:     2019.05.15
# PURPOSE:  Creates a plate object and returns an
#           array of the objects.
#
# NOTES:    The code .
##

# Imports python modules
import pandas as pd
from apm_logging import MyLogger


class Plate:
    """
    Object class for working with assay and reagent
    plates in the APmaker program.
    """
    def __init__(self, barcode, well_count, part_num):
        """
        Initializes the class values and populates the
        plate information (e.g. barcode, no of wells, part no.)
        """
        self.barcode = barcode
        self.well_count = well_count
        self.part_num = part_num


@MyLogger
def read_plate_file(file_name):
    """
    Reads through the csv file designated in the location
    variable and returns a list of plate objects.
    """

    # Read through the barcode file (Excel) to obtain each barcode
    # (per line) and store the barcodes as keys in the plate list.
    try:
        plates = pd.read_excel(file_name)
    except ValueError:
        print('There was an error reading the plate file.')

    # Loop through the barcodes and create a dict of plate objects
    plate_dict = {}
    for _, plate in plates.iterrows():
        plate_dict[plate['barcode']] = Plate(plate['barcode'],
                                             plate['well_count'],
                                             plate['part_num'])

    # return the dictionary of plate objects
    return plate_dict
