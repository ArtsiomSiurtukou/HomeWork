text = input('Введите свой текст в программу. \nОна заменит пробелы в Вашем тексте на символ "-" - ')
text_mod = ''.join('-' if i == ' ' else i for i in text)
print(text_mod + '\nКонец программы')
