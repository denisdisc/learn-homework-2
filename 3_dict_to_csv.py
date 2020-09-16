"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv




def main():
    user_list = [
        {'experience': '1 year', 'name': 'Antony', 'age': '23', 'job': 'manager'},
        {'experience': '4 years', 'name': 'Bob', 'age': '28', 'job': 'oil indastry worker'},
        {'experience': '8 years', 'name': 'Chris', 'age': '32', 'job': 'seller'},
        {'experience': '2 years', 'name': 'Mark', 'age': '26', 'job': 'engineer'},
        {'experience': '0 year', 'name': 'Vasily', 'age': '21', 'job': 'student'},
    ]
    with open('users.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job', 'experience']
        writer = csv.DictWriter(f, fields, delimiter = ';')
        writer.writeheader()
        for user in user_list:
            writer.writerow(user)
        

if __name__ == "__main__":
    main()
