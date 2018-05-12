import json
import math
import argparse


def get_bar_info(bar):
    info = 'Name: {} \n Adress: {} \n Seats amount: {} \n'
    return info.format(bar['Name'], bar['Address'], bar['SeatsCount'])


def load_data(filepath):
    return json.loads(open(filepath, 'r', encoding='cp1251').read())


def get_biggest_bar(bars_list):
    return max(bars_list, key=lambda x: x['SeatsCount'])


def get_smallest_bar(bars_list):
    return min(bars_list, key=lambda x: x['SeatsCount'])


def get_distance(bar_info, longitude, latitude):
    bar_lon, bar_lat = float(bar_info["Latitude_WGS84"]),\
                       float(bar_info["Longitude_WGS84"])
    return math.sqrt((longitude - bar_lon) ** 2 + (latitude - bar_lat) ** 2)


def get_closest_bar(bars_list, longitude, latitude):
    return min(bars_list, key=lambda x: get_distance(x, longitude, latitude))


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file_path", type=str,
        help="path of the json file with bars info, you can get one on your "
             "open data .gov site"
    )
    return parser

if __name__ == '__main__':
    args = get_parser().parse_args()
    bars = load_data(args.file_path)
    message = 'Print coordinates separated by space (latitude first): \n'
    lon, lat = (float(x) for x in input(message).split())
    print('Nearest: \n', get_bar_info(get_closest_bar(bars, lon, lat)))
    print('Biggest: \n', get_bar_info(get_biggest_bar(bars)))
    print('Smallest: \n', get_bar_info(get_smallest_bar(bars)))
