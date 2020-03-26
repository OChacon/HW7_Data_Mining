"""
Authors: Tyler Angelo, Oscar Chacon
Emails: orc2815@rit.edu
Title: HW07_Agglomerate.py
Description:
"""

# Imports
import os
import sys
import numpy as np
import pandas as pd


def calculate_correlations(data_frame):
    """
    Title: calculate_correlations
    :param data_frame: the pandas data_frame that was created from parsing the csv file
    :return: max_corr: The maximum correlation value
    :return: max_index: The maximum correlation index
    :return: min_corr: The minimum correlation value
    :return: min_index: The minimum correlation index
    Description: This method calculates all the correlations with the sickness column, and picks out the item
    that has the highest correlation, and the item that has the lowest correlation.
    """
    correlations = data_frame.corr()
    sick_corrs = correlations['Sickness']
    max_corr = -1
    min_corr = 1
    max_index = 0
    min_index = 0
    index = 0
    for corr in sick_corrs:
        if corr > max_corr and corr != 1:
            max_corr = corr
            max_index = index
        elif corr < min_corr and corr != -1:
            min_corr = corr
            min_index = index
        index += 1

    return max_corr, max_index, min_corr, min_index


if __name__ == '__main__':
    """
    Title: main
    Description: The main method for this file. First reads in the given file parameter, parses the
    data, and then writes a training file based off the training data given from the file parameter.
    """
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    split_path = path.split("\\")
    split_path = split_path[:len(split_path) - 1]
    training_file_path = ""
    for path in split_path:
        training_file_path += os.path.join(path) + "\\"
    training_file = None
    try:
        training_file = open(os.path.join(training_file_path, sys.argv[1]), "r")
    except FileNotFoundError as e:
        print(e)
        print("Note* This program assumes that the data file is located in the directory above its current one.")
        print("This program will automatically find the pathing, all that is needed is the file's name as a parameter")
        exit(1)
    except IndexError:
        print("Please Enter in the data file's name as a parameter.")
        exit(1)
    data_frame = pd.read_csv(training_file)


