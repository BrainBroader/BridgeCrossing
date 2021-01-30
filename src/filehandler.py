""" A module containing utility functions for handling files. """

import os
import csv


def read_csv(path):
    """ Reads a csv file and converts it into a dictionary object.

    Args:
        path:
             A string representing the path to the csv file.

    Returns:
        A dictionary object containing the record of the csv file.
    """
    if path is None:
        print("[ERROR] filehandler.read_csv - Null object passed")
        return None

    if not os.path.exists(path):
        print("[ERROR] filehandler.read_csv - " + path + " doesn't exist")
        return None

    if not path.endswith(".csv"):
        print("[ERROR] filehandler.read_csv - " + path + " isn't of CSV format")
        return None

    try:
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # skip header line
            records = {}
            for rows in csv_reader:
                records[rows[0]] = int(rows[1])
    except IOError:
        print("[ERROR] filehandler.read_csv - Couldn't read from file " + path)
        return None

    return records
