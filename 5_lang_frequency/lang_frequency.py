import argparse
import re
import os
from collections import Counter


def get_text(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return file.read().lower()


def get_most_frequent_words(text, printcounter):
    rgx = re.compile("(\w[\w']*\w|\w)")
    word_list = rgx.findall(text)
    return Counter(word_list).most_common(printcounter)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filepath", type=str,
        help="path to file with text"
    )
    return parser


if __name__ == '__main__':
    printcounter = 10
    args = get_parser().parse_args()
    text = get_text(args.filepath)
    if text:
        for word, amount in get_most_frequent_words(text, printcounter):
            print('{} : {}'.format(word, amount))
    else:
        print("Where's no such file or directory: {}".format(args.filepath))
