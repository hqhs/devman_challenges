# Prettify JSON

Purpose of this project is output .json files in human-readable form.

# Quickstart

Use python (3.5+) to run pprint_jsot.py in your terminal with <file_path> as
argument. load_data(filepath) returns data in .json format, and
pretty_print_json(data) prints .json data in human-readable form.

Example of script launch on Linux, Python 3.5:

```#!bash
$ cat ./data.json
{"testlist":["test1","test2","test3","test4","test5"]}
$ python pprint_json.py ./data.json
{
    "testlist": [
        "test1",
        "test2",
        "test3",
        "test4",
        "test5"
    ]
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
