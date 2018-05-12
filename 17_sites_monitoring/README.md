# Sites Monitoring Utility

This script scan threw each domain from text file, and output domain status:
if domain respond with [200](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) and domain name is paid more then for a month, then script
ouput 'OK', and 'probably NOT OK' otherwise. 

```#!bash
$python3 check_sites_health.py sites.txt
google.com : OK
91.ru : OK
vk.com : OK
facebook.com : OK
stackoverflow.com : OK
dimaska.com : probably NOT OK

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
