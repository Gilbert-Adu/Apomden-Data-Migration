import csv, json

"""
This python script contains code for converting a csv file into a json as a
list of dictionaries.
To run this code, you need the CSV and JSON libraries.

This is my first work for Apomden, a Ghanaian health startup
"""

def formatJSON(csvpath, jsonfilepath):

    """
    Obtain data from csv file in sam location as this file.
    """

    data = {}
    my_list = []
    with open(path) as file:
        csvReader = csv.DictReader(file)
        for csvRow in csvReader:

            data = csvRow
            my_list.append(data)

    """

    Write retrieved data into a json file
    NOTE: json file is automatically created when code is run from terminal
    and updates each time it run again.
    """


    with open(jsonfilepath,"w") as jsonfile:

        jsonfile.write(json.dumps(my_list,indent=4))

path = 'Merged data - Hospitals.csv'
jsonfilepath = 'merged.json'

formatJSON(path, jsonfilepath)
