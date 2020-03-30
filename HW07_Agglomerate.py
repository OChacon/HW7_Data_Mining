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
    Description: This method calculates all the correlations with the sickness column, and picks out the item
    that has the highest correlation, and the item that has the lowest correlation.
    """
    data_frame = data_frame.drop(columns=['ID'])
    correlations = data_frame.corr()
    list_of_column_names = list(correlations.columns.values)
    # Min is rice with soda
    # print(correlations)
    # correlations.to_csv('correlations.csv', index=False)

    # Find the highest correlation between two attributes
    max_corr_value = -1
    first_attr_name = ''
    second_attr_index = 0
    for attr in correlations:
        index_tracker = 0
        for corr in correlations[attr]:
            if corr > max_corr_value and corr != 1:
                max_corr_value = corr
                first_attr_name = attr
                second_attr_index = index_tracker
            index_tracker += 1

    second_attr_name = list_of_column_names[second_attr_index]
    print('The highest correlation is between attributes ' + first_attr_name + ' and ' + second_attr_name +
          ' with a value of ' + str(max_corr_value))

    # Find which attribute fish has the highest correlation with
    fish_max_corr_value = -1
    fish_attr_index = 0
    index_tracker = 0
    for corr in correlations['  Fish']:
        if corr > fish_max_corr_value and corr != 1:
            fish_max_corr_value = corr
            fish_attr_index = index_tracker
        index_tracker += 1

    fish_attr_name = list_of_column_names[fish_attr_index]
    print('Fish has the highest correlation with attribute ' + fish_attr_name + ' with a value of ' +
          str(fish_max_corr_value))

    # Find which attribute meat has the highest correlation with
    meat_max_corr_value = -1
    meat_attr_index = 0
    index_tracker = 0
    for corr in correlations['  Meat']:
        if corr > meat_max_corr_value and corr != 1:
            meat_max_corr_value = corr
            meat_attr_index = index_tracker
        index_tracker += 1

    meat_attr_name = list_of_column_names[meat_attr_index]
    print('Meat has the highest correlation with attribute ' + meat_attr_name + ' with a value of ' +
          str(meat_max_corr_value))

    # Find which attribute beans has the highest correlation with
    beans_max_corr_value = -1
    beans_attr_index = 0
    index_tracker = 0
    for corr in correlations[' Beans']:
        if corr > beans_max_corr_value and corr != 1:
            beans_max_corr_value = corr
            beans_attr_index = index_tracker
        index_tracker += 1

    beans_attr_name = list_of_column_names[beans_attr_index]
    print('Beans has the highest correlation with attribute ' + beans_attr_name + ' with a value of ' +
          str(beans_max_corr_value))

    # Find which attribute is least correlated with all other attributes
    average_corr_values = []
    for attr in correlations:
        sum = 0
        for corr in correlations[attr]:
            sum += corr
        average_corr_values.append(sum/len(list_of_column_names))

    lowest_average_value = 1
    lowest_average_index = 0
    index_tracker = 0
    for average in average_corr_values:
        if average < lowest_average_value:
            lowest_average_value = average
            lowest_average_index = index_tracker
        index_tracker += 1

    lowest_average_attr_name = list_of_column_names[lowest_average_index]
    print('The first attribute that is least correlated with all other attributes is ' + lowest_average_attr_name +
          ' with an average correlation value of ' + str(lowest_average_value))

    # Find the second attribute that is least correlated with all other attributes
    second_lowest_average_value = 1
    second_lowest_average_index = 0
    index_tracker = 0
    for average in average_corr_values:
        if average < second_lowest_average_value and index_tracker != lowest_average_index:
            second_lowest_average_value = average
            second_lowest_average_index = index_tracker
        index_tracker += 1

    second_lowest_average_attr_name = list_of_column_names[second_lowest_average_index]
    print('The second attribute that is least correlated with all other attributes is ' +
          second_lowest_average_attr_name + ' with an average correlation value of ' + str(second_lowest_average_value))

    agglomeration(data_frame)
    #Send max corr features as well


def agglomeration(correlations):
    clusters_list = []
    for item in correlations:
        clusters_list.append([])



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
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_columns', 1000)
    calculate_correlations(data_frame)
