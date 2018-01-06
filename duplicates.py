#!/usr/bin/env python3


import os
import collections
import sys


def get_directory_content(directory_path):
    files_stats_list = []
    for directory, _, files in os.walk(directory_path):
        for file_name in files:
            filepath = os.path.join(directory, file_name)
            filesize = os.stat(filepath).st_size
            files_stats_list.append(
                {
                    "file_name": file_name,
                    "directory": directory,
                    "file_size": filesize
                }
            )
    return files_stats_list


def get_file_benchmark(file_stat):
    file_name = file_stat["file_name"]
    file_size = file_stat["file_size"]
    file_benchmark = (file_name, file_size)
    return file_benchmark


def count_files_stats(files_stats_list):
    files_benchmarks_stats_list = [
        get_file_benchmark(file_stat)
        for file_stat in files_stats_list
    ]
    files_stats_counter = collections.Counter(
        files_benchmarks_stats_list
    )
    return files_stats_counter


def get_list_of_dublicates(files_stats_list):
    files_stats_counter = count_files_stats(
        files_stats_list
    )
    dublicating_files_stats_list = [
        file_stat for file_stat in files_stats_list
        if files_stats_counter[
            get_file_benchmark(file_stat)
        ] > 1
    ]
    dublicating_files_stats_list.sort(key=get_file_benchmark)
    return dublicating_files_stats_list


def print_dublicated_files_stats(dublicating_files_stats, directory_path):
    print(
        "--------------------------------------------------"
        "\nСписок дублирующихся файлов в каталоге {} :"
        "\n--------------------------------------------------".format(
            directory_path
        )
    )
    for file_stat_record in dublicating_files_stats:
        print("{}/{}".format(
            file_stat_record["directory"],
            file_stat_record["file_name"]
        ))


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
        files_stats_list = get_directory_content(directory_path)
        dublicating_files_stats_list = get_list_of_dublicates(files_stats_list)
        print_dublicated_files_stats(
            dublicating_files_stats_list,
            directory_path
        )
