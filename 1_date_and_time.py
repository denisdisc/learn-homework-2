import datetime
import locale

"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    dt_now = datetime.datetime.now().date()
    delta1 = datetime.timedelta(days=1)
    delta30 = datetime.timedelta(days=30)
    print(f'Вчера: {dt_now - delta1}')
    print(f'Сегодня: {dt_now}')
    print(f'30 дней тому назад: {dt_now - delta30}')


def str_2_datetime(date_string):
    date_dt = datetime.datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    print(date_dt)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
