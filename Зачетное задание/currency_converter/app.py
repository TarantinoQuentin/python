import requests
import os
import json
import string


VALID_CHARS = string.digits + '.'


def is_valid_key() -> str:
    """
    Функция проверяет существование файла и записанный в нем ключ.
    Если ключа или файла нет, то создает и принимает от пользователя ключ,
    записывает в файл.

    :return: Возвращает ключ.
    """
    if os.path.exists('key_access.txt') and os.path.isfile('key_access.txt'):
        with open('key_access.txt', 'r+', encoding='utf-8') as key_file:
            true_key = key_file.read()
            if true_key:
                print('Найден сохраненный ключ.')
                print()
            else:
                true_key = input('Ключ не найден, введите ключ: ')
                print()
                key_file.write(true_key)
        return true_key
    else:
        with open('key_access.txt', 'w', encoding='utf-8') as key_file:
            true_key = input('Ключ не найден, введите ключ: ')
            print()
            key_file.write(true_key)
        return true_key


def is_valid_currency_code(input_code: str) -> bool:
    """
    Функция проверяет, что валютный код содержится в базе кодов.
    :param input_code: Вводимый пользователем код.
    :return: Возвращает True или False в зависимости от того, содержится ли
    код в базе.
    """
    with open('currency.json', encoding='utf-8') as file:
        codes_data = json.load(file)
        codes_list = [currency['код'] for currency in codes_data['валюты']]
        if input_code not in codes_list:
            print('Код валюты не найден, ознакомьтесь со списком:', '\n')
            for code_info in codes_data['валюты']:
                print(f'{code_info['код']} — {code_info['название']}, {code_info['страна']}')
            print()
            return False
        else:
            return True


def is_valid_sum(input_sum: str) -> float:
    """
    Функция проверяет, что введенное значение суммы для конвертации
    отвечает необходимым требованием и подлежит преобразованию в тип float.
    :param input_sum: Вводимая пользователем сумма.
    :return: Возвращает сумму, преобразованную в тип данных float.
    """
    dots_count = 0
    minus_count = 0
    invalid_chars = 0
    input_sum = input_sum.strip()
    for char in input_sum:
        if char == '-':
            minus_count += 1
        elif char not in VALID_CHARS:
            invalid_chars += 1
        elif char == '.':
            dots_count += 1
    if input_sum == '':
        print('Значение не должно быть пустым.')
        return False
    elif dots_count > 1:
        print('Много точек.')
        return False
    elif minus_count > 0:
        print('Число должно быть положительным.')
        return False
    elif invalid_chars > 0:
        print('Число должно содержать только цифры и максимум одну точку.')
        return False
    try:
        1 / float(input_sum)
    except ZeroDivisionError:
        print('Число должно быть больше ноля.')
        return False
    else:
        return True


def get_response(valid_key: str, base_code: str) -> list:
    """
    Функция отправляет запрос на сайт.
    :param valid_key: Ключ доступа к сайту.
    :param base_code: Валютный код, от которого будем конвертировать.
    :return: Возвращает список валютных кодов и суммы за основную валюту.
    """
    url = f"https://v6.exchangerate-api.com/v6/{valid_key}/latest/{base_code}"
    response = requests.get(url)
    currency_data = response.json()['conversion_rates']
    return currency_data


print('''
Добро пожаловать в приложение для конвертации валют!
''')

key = is_valid_key()

while True:
    if not is_valid_currency_code(currency_code := input('Введите код исходной валюты (например, USD): ')):
        continue
    break
while True:
    if not is_valid_currency_code(target_code := input('Введите код целевой валюты (например, RUB): ')):
        continue
    break

while True:
    if not is_valid_sum(sum_to_convert := input('Введите сумму для конвертации: ')):
        continue
    break

print()
sum_to_convert = round(float(sum_to_convert), 2)
data = get_response(key, currency_code)

result_sum = float(sum_to_convert) * float(data[target_code])
print(f'За {sum_to_convert:.2f} {currency_code} вы получите {round(result_sum, 2):.2f} {target_code}.')
