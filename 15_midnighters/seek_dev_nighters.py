from datetime import datetime
import argparse

import requests
import pytz


def load_attempts(url, page_number):
    payload = {'page': page_number}
    response = requests.get(url, params=payload)
    return response.json()['records']


def is_night(time):
    hour_then_night_ends = 6
    return time.hour < hour_then_night_ends


def is_nighter(persona):
    timestamp = persona['timestamp']
    username = persona['username']
    tzone = persona['timezone']
    if timestamp:
        users_tz = pytz.timezone(tzone)
        utc_time = datetime.utcfromtimestamp(timestamp)
        loc_dt = users_tz.localize(utc_time)
        return is_night(loc_dt)
    else:
        return False


def get_midnighters(participants):
    midnighters = filter(is_nighter, participants)
    names = set([persona['username'].encode('utf-8')
        for persona in midnighters])
    return names


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pages', type=int, default=1, 
            help='amount of pages to check')
    return parser.parse_args()


if __name__ == '__main__':
    url_attempts = 'https://devman.org/api/challenges/solution_attempts/'
    participants = []
    pages = args.pages
    for page_number in range(1, pages):
        one_page = load_attempts(url_attempts, page_number)
        participants.extend(one_page)
    midnighters = get_midnighters(participants)
    output = 'These guys are midnighters: {}'.format(', '.join(midnighters))
    print(output)
