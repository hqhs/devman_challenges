import argparse
import requests
from datetime import date
from dateutil.relativedelta import relativedelta
from collections import OrderedDict

import whois


def load_urls4check(path):
    with open(path, 'r') as file:
        urls = [url.strip('\n') for url in file.readlines()]
        return urls


def is_server_respond_with_200(url):
    try:
        responce = requests.get(''.join(['http://', url]))
        return responce.ok
    except requests.exceptions.ConnectionError:
        return False


def get_domain_expiration_date(domain_name):
    domain = whois.whois(domain_name)
    if isinstance(domain.expiration_date, list):
        paid_till = 1
        e_date = domain.expiration_date[paid_till].date()
    else:
        e_date = domain.expiration_date.date()
    return e_date


def check_domain_expiration_date(expiration_date):
    month_from_now = date.today() + relativedelta(months=+1)
    return expiration_date >= month_from_now


def check_url(url):
    is_reachable = is_server_respond_with_200(url)
    if is_reachable:
        date = get_domain_expiration_date(url)
        return check_domain_expiration_date(date)
    else:
        return False


def check_list(urls_list):
    results = OrderedDict.fromkeys(urls_list)
    for url in urls_list:
        status = 'OK' if check_url(url) else 'probably NOT OK'
        results[url] = status
    return results


def output_results(urls_status):
    output_string = '{} : {}'
    for url, status in urls_status.items():
        print(output_string.format(url, status))


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='path to file with domen names')
    return parser


if __name__ == '__main__':
    args = get_parser().parse_args()
    urls_list = load_urls4check(args.file_path)
    urls_statuses = check_list(urls_list)
    output_results(urls_statuses)
