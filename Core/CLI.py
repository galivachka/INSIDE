import pyinputplus as pyip
from Config import *
from Run import start_async_attacks
import colorama
from colorama import Fore, Style
import pyfiglet
import os
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colorful(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)

def animated_clear():
    for _ in range(30):
        time.sleep(0.05)
        clear_terminal()

def main():
    '''Основная функция'''

    # Инициализация colorama для поддержки цветов в терминале
    colorama.init()

    # Анимация очистки терминала
    animated_clear()

    # Анимированный ASCII-артовый заголовок
    print(Fore.CYAN + pyfiglet.figlet_format('SHKUR  BOMBER', font='slant'))

    # Запрос номера телефона 
    print_colorful('Введите номер без знака "+": ', Fore.YELLOW)
    number = pyip.inputStr(prompt='')

    # Запрос типа атаки
    print_colorful('\nВыберите тип атаки:', Fore.CYAN)
    type_attack = pyip.inputMenu(['MIX', 'SMS', 'CALL'], numbered=True)

    # Запрос количества кругов
    print_colorful('\nВведите количество кругов (по умолчанию 1):', Fore.MAGENTA)
    replay = pyip.inputInt(default=1)

    # Запуск атаки
    print_colorful('\nЗапуск атаки...', Fore.GREEN)
    start_async_attacks(number, replay)

if __name__ == "__main__":
    main()
