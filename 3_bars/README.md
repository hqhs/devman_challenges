# Ближайшие бары

Скрипт запрашивает координаты и выводит ближайший к ним бар, а так же самый
большой и самый маленькие бары, работает только в Москве, и частично в
московской области.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии
3.5, а так же .json файла с даннами о барах в вашем районе (список
московских баров можно скачать [тут](https://data.mos.ru/opendata/7710881420-bary))


Запуск на Linux:

```#!bash

$ python bars.py ./data-2897-2016-11-23.json # possibly requires call of
python3 executive instead of just python
Print coordinates separated by space (latitude first):
55.7900312 37.6742982
Nearest:
 Name: Бар «Rainbow Pub»
 Adress: Сокольническая площадь, дом 4, корпус 1-2
 Seats amount: 40

Biggest:
 Name: Спорт бар «Красная машина»
 Adress: Автозаводская улица, дом 23, строение 1
 Seats amount: 450

Smallest:
 Name: БАР. СОКИ
 Adress: Дубравная улица, дом 34/29
 Seats amount: 0
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
