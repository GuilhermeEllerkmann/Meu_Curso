import locale
import os

locale.setlocale(locale.LC_ALL, '')


def money_converter(amount):
    money_number = locale.currency(amount, symbol=True, grouping=True)
    return money_number


def number_converter(number):
    number_converted = locale.format_string('%d', number, grouping=True)
    return number_converted


start = 0

while True:
    os.system('cls')
    valor = int(
        input(
            'Aqui sera feita uma calculadora que soma valores monetarios.\n'
            'Digite o primeiro valor: '
        )
    )
    start += valor
    choice = str(
        input('Deseja digitar um outro valor? S para sim, N para nao: ')
    ).upper()

    if choice == 'S':
        continue
    else:
        print(money_converter(start))
        start = 0
        break
