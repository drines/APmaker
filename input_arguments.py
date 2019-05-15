#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.15
# REVISED DATE:     2019.05.15
# PURPOSE:  Takes in any command line arguments
#
# NOTES:    Arguments controlling logging level and the
#           location of files containing details for any
#           consumables, cell lines or reagents needed.
##

# Imports python modules
import argparse


def get_input_args():
    """
    Retrieves and parses the command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these command line arguments. If 
    the user fails to provide some or all of the arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser(description='Classifies pet images using a ' +
            'pretrained CNN model, compares these classifications to the true ' +
            'identity of the pets in the images, and summarizes how well the CNN ' +
            'performed on the image classification task.')
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('--dir', type=str, default='pet_images/', help='directory ' +
                        'name for the Image Folder (default: \'pet_images\').')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN model ' +
                        'architecture. Options are: resnet, alexnet or vgg ' +
                        '(default: \'vgg\').')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='Text ' +
                        'file with the dog names (default: \'dognames.txt\').')
    
    # Return the parsed arguments back to the calling function
    return parser.parse_args()
