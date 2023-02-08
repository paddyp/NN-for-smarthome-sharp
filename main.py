# create Testdata for Neuronal Network
#
#   The input vector must have the following data
#   [(direction_vector xyz), angle, distance, weekday, current_time, (current_values_smart_devices) ]
#
#   The output vector must have the following data
#   [(relevance devices < 0.6 irrelevant, > 0.8 relevant), [Interfaces with Relvance, highest relevance is taken](size m)]

import os

from helper import clean_path
from scenarios import szenario_1_data


def _save_file(data: list, filename: str, postfix="txt", path="export") -> None:
    path = clean_path(path)
    fullname = filename + "." + postfix
    fullpath = "./" + path + fullname

    if not os.path.isdir(path):
        os.makedirs(path)
    f = open(fullpath, "w+")
    for dat in data:
        f.write(",".join([str(x) for x in dat]))
        f.write("\n")
    f.close()


def create_training_data(data: tuple) -> None:
    train_x, train_y = data
    _save_file(train_x, "train_x")
    _save_file([train_y], "train_y")


def create_test_data(data: list) -> None:
    test_x, test_y = data
    _save_file(test_x, "test_x")
    _save_file([test_y], "test_y")


if __name__ == "__main__":
    create_training_data(szenario_1_data(2))
