""" A module containing utility functions for handling files. """

import csv


def read_csv(path):
    """ Reads a csv file and converts it into a dictionary object.

    Args:
        path:
             A string representing the path to the csv file.

    Returns:
        A dictionary object containing the record of the csv file.
    """
    csv_file = open(path, 'r')
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip header line
    records = {}
    for rows in csv_reader:
        records[rows[0]] = int(rows[1])

    return records
