#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.15
# REVISED DATE:     2019.05.16
# PURPOSE:   Creates the json file
#
# NOTES:     Takes in the autoprotocol object and 
#            dumps the json output to a text file.
##

# Imports python modules
import json


def dump_json(containers):
    """
    Function to output the autoprotocol json instructions
    """
    for key in containers:
        with open("json\\" + containers[key].barcode + ".json", 'w') as json_file:
            json.dump(containers[key].p.as_dict(), json_file, indent=2)
