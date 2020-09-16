"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as first, open('referat2.txt', 'w', encoding='utf-8') as second:
        content = 0
        for line in first:
            content += len(line)
            line = line.replace('.', '!')
            second.write(line)
        print(f'В этом тексте {content} знаков.')

if __name__ == "__main__":
    main()
