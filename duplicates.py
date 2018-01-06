#!/usr/bin/env python3


import os
import collections
import sys


def get_dict_with_files_records(directory_path):
    dict_with_files_records = collections.defaultdict(list)
    for directory, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(directory, file_name)
            file_size = os.stat(file_path).st_size
            dict_with_files_records[(file_name, file_size)].append(file_path)
    return dict_with_files_records


def get_dict_with_dublicating_files_records(dict_with_files_records):
    dict_with_dublicating_files_records = {}
    for file_characteristics, pathes in dict_with_files_records.items():
        if len(pathes) > 1:
            dict_with_dublicating_files_records[
                file_characteristics
            ] = pathes
    return dict_with_dublicating_files_records


def print_dublicated_files_records(
    dict_with_dublicating_files_records,
    directory_path
):
    print(
        "**************************************************"
        "\n"
        "дублирующиеся файлы в директории {} :"
        "\n"
        "**************************************************".format(
            directory_path
        )
    )
    for (
        file_characteristics,
        pathes
    ) in dict_with_dublicating_files_records.items():
        for path in pathes:
            print("{}".format(
                    path
                ))
        print("--------------------------------------------------")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(
            "Не указан аргумент - имя директории."
            "\nПерезапустите скрипт командой в формате "
            "'python3 lang_frequency.py <path to directory>'")
    directory_path = sys.argv[1]
    if not os.path.exists(directory_path):
        print("Такая директория не существует")
    else:
        dict_with_files_records = get_dict_with_files_records(
            directory_path
        )
        dict_with_dublicating_files_records = (
            get_dict_with_dublicating_files_records(
                dict_with_files_records
            )
        )
        print_dublicated_files_records(
            dict_with_dublicating_files_records,
            directory_path
        )
