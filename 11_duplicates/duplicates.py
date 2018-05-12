import os
import argparse
import hashlib
from collections import defaultdict


def calculate_hash_for(file_path):
    md5 = hashlib.md5()
    kb = 65536
    with open(file_path, 'rb') as file_:
        for chunk in iter(lambda: file_.read(kb), b''):
            md5.update(chunk)
    return md5.hexdigest()


def find_duplicates(file_names):
    duplicates = defaultdict(list)
    for file_name in file_names:
        file_hash = calculate_hash_for(file_name)
        duplicates[file_hash].append(file_name)
    return duplicates


def get_files_from_dirtree(file_path):
    file_names = []
    for root, _, files in os.walk(file_path):
        new_names = [os.path.join(root, file_name) for file_name in files]
        file_names.extend(new_names)
    return file_names


def get_argument_parser():
    parser = argparse.ArgumentParser(
        description="find and delete allduplicate files"
    )
    parser.add_argument(
        "file_path", type=str,
        help='dir name where you need to find duplicates'
    )
    return parser


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    file_names = get_files_from_dirtree(args.file_path)
    duplicates = find_duplicates(file_names)
    for value in duplicates.values():
        print("\nThese files are the same: {}".format(", ".join(value)))
