import json
import logging
import sys

logging.basicConfig(format='%(message)s', level=logging.INFO)


def load_data(filepath):
    with open(filepath, 'r', encoding='cp1251') as json_file:
        json_content = json_file.read()
        logging.debug(json_content)
        return json_content


def pretty_print_json(data_in_json_format):
    decoded_data = json.loads(data_in_json_format)
    logging.debug(decoded_data)
    print(json.dumps(decoded_data, ensure_ascii=False, sort_keys=True,
                     indent=4))


if __name__ == '__main__':
    logging.debug('main works')
    if len(sys.argv) == 1:
        file_path = input('print path to the file:\n')
        data_in_json_format = load_data(file_path)
        pretty_print_json(data_in_json_format)
    elif len(sys.argv) == 2:
        file_path = str(sys.argv[1])
        data_in_json_format = load_data(file_path)
        pretty_print_json(data_in_json_format)
    else:
        logging.debug(str(sys.argv))
        print("too much arguments in input, try again")

