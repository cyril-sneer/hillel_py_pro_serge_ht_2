"""
This module contains functions, we need for our Flask-application:
get_text_file()
get_fake_users()
calc_average_height_and_weight()
"""

import faker
import csv
import requests


# Constants declaration
CM_IN_INCH = 2.54
KG_IN_POUNDS = 0.453592


def get_text_file(txt_file_name: str) -> list[str]:
    """
    This one reads the <file_name> and returns its content as a list of strings

    :param txt_file_name:
    :return: list of strings
    """

    try:
        with open(txt_file_name, 'r') as txt_file:
            str_list = [line.strip() for line in txt_file]  # read the file
    except FileNotFoundError:
        str_list = ['Error occur! File requirements.txt not found.']

    return str_list


def get_fake_users(quantity: int) -> list[str]:
    """
    This one generates <quantity> fake usernames with email address using the Faker lib

    :param quantity:
    :return: list of strings
    """

    fake = faker.Faker()
    return [f'{num} - {fake.name()} - {fake.email()}' for num in range(1, quantity + 1)]


def calc_average_height_and_weight(csv_file_name: str) -> (float, float):
    """
    This reads a file containing people's height and weight data.
    Calculates average values in centimeters and kilograms

    :param csv_file_name:
    :return: <average height in centimeters>, <average weight in kilos>
    """

    with open(csv_file_name, newline='') as csv_file:  # open CSV file
        csv_reader = csv.reader(csv_file)  # get iterator

        counter = total_height = total_weight = 0

        csv_reader.__next__()  # skip the first (title) line
        for line in csv_reader:
            if line:
                counter += 1
                total_height += float(line[1])
                total_weight += float(line[2])

        average_height = round((total_height / counter) * CM_IN_INCH, 2)
        average_weight = round((total_weight / counter) * KG_IN_POUNDS, 2)

    return average_height, average_weight


def get_astros(json_link: str) -> tuple[int, list[str]]:
    """
    This one gets json data with astronauts names.

    :param json_link:
    :return: astronauts quantity as int, and their names as list of strings
    """
    try:
        astros_request = requests.get(json_link)  # get request
    except:
        return 0, ['Something goes wrong..']
    else:
        astros = astros_request.json()['people']
        astro_list = [astro['name'] for astro in astros]
        astro_qty = len(astro_list)
        return astro_qty, astro_list

