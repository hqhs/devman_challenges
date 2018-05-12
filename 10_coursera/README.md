# Coursera Dump

This script takes 20 random coursera courses from their [xml feed](https://www.coursera.org/sitemap~www~courses.xml).
Then takes name, language, start date, amount of weeks, and avarage user rating, and save them to xlsx file in the 
same directory, where script runned. AMOUNT is amount of courses, 5 if it's not declared, and NAME is name of output 
file. 

```#!bash
$ usage: python3  coursera.py [-h] [-a AMOUNT] [-n NAME]

optional arguments:
  -h, --help            show this help message and exit
  -a AMOUNT, --amount AMOUNT
  -n NAME, --name NAME
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
