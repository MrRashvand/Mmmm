# decode by @felix_335

import os
import ctypes
import time
import re
import requests
import json
from colorama import init, Fore, Back, Style
import webbrowser
url = 'https://youtube.com/shorts/SXHMnicI6Pg?si=OXM4gp_ZkndfiMXz'
webbrowser.open(url)
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls')
menu_principal = '\n ██ ▄█▀▄▄▄       ██▀███   ███▄ ▄███▓ ▄▄▄        ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ \n ██▄█▒▒████▄    ▓██ ▒ ██▒▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒\n▓███▄░▒██  ▀█▄  ▓██ ░▄█ ▒▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░\n▓██ █▄░██▄▄▄▄██ ▒██▀▀█▄  ▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ \n▒██▒ █▄▓█   ▓██▒░██▓ ▒██▒▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓\n▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒\n░ ░▒ ▒░ ▒   ▒▒ ░  ░▒ ░ ▒░░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░\n░ ░░ ░  ░   ▒     ░░   ░ ░      ░     ░   ▒   ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░\n░  ░        ░  ░   ░            ░         ░  ░      ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░                                                                      ░  \n\n    DECODE BY @FELIX_335'

class leaked:
    
    def hash(self, hash):
        text = requests.get('https://hashtoolkit.com/reverse-hash/?hash=' + hash).text
        passw = re.findall('/generate-hash/\\?text=(.*?)\\"', text)
        if len(passw) != 0:
            passw = passw[0]
            return passw
        passw = None
        return passw

    
    def email(self, email):
        dataList = []
        req = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/' + email, headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'LittleBr0ther' })
    


warning = '[' + Fore.RED + '!' + Fore.RESET + ']'
question = '[' + Fore.YELLOW + '?' + Fore.RESET + ']'
found = '[' + Fore.GREEN + '+' + Fore.RESET + ']'
information = '[' + Fore.BLUE + 'I' + Fore.RESET + ']'
wait = '[' + Fore.MAGENTA + '*' + Fore.RESET + ']'

def searchGoogle(requete, requete2 = ('', '')):
    pass
# decode by @Felix_335


def google():
    print('\n' + information + ' Введите имя, фамилию, город, вид спорта, школу... \n (Чем больше информации вы введете, тем точнее будет поиск.)\n')
    nom = input(Fore.RED + '  [Karma] ' + Fore.WHITE + 'Введите данные:' + Fore.WHITE)
    print('\n' + wait + ' Ищу информацию...')
    url = 'https://www.google.com/search?num=20&q=\\%s\\'
    lista = ''
    nom2 = nom.split()
    if len(nom2) == 0:
        print()
        print(Fore.RED + '[!]' + Fore.GREEN + ' Параметры отсутствуют...')
        print()
        return None
    longi = str(nom2[-1])
# decode by @felix_335


def SearchEmail():
    print()
    email = input(Fore.RED + '  [Karma] ' + Fore.WHITE + 'Введите адрес электронной почты:' + Fore.WHITE)
    print('\n' + wait + " Пытаюсь получить информацию из электронной почты '%s'..." % email)
    lkd = leaked()
    leak = lkd.email(email)
# decode felix_335


def searchUserName():
    print()
    username = input(Fore.RED + '  [Karma]' + Fore.WHITE + ' Введите ник: ' + Fore.WHITE)
    print('\n  ' + wait + " Buscando información de '%s'..." % username)
    url = 'https://www.google.com/search?num=100&q=\\%s\\'
    url2 = 'https://www.google.com/search?num=100&q=\\intitle:"%s"\\'
    requete = requests.get(url % username)
    requete2 = requests.get(url2 % username)
    searchGoogle(requete = requete, requete2 = requete2)

menu = '  [1] - Поиск пароля почты\n  [2] - Поиск по нику\n  [3] - Поиск по IP\n  [4] - Поиск по Google Frame Works\n  [5] - Поиск по нику Minecraft\n  [CTRL + C] - Выход\n'
print(Fore.RED + menu_principal)
print(Fore.WHITE + menu)
parametros = input(Fore.WHITE + ' root@karma > ' + Fore.WHITE)
if parametros == '1':
    SearchEmail()
elif parametros == '2':
    searchUserName()
elif parametros == '3':
    print()
    target = input('Введите IP...')
    url = 'http://ip-api.com/json/'
    response = requests.get(url + target)
    data = response.text
    jso = json.loads(data)
    print()
    print(f'''{Fore.WHITE} IP: ''' + target)
    print(f'''{Fore.WHITE} ISP: ''' + jso['isp'])
    print()
    print(f''' {Fore.MAGENTA}[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE} Страна: ''' + jso['country'] + ' - TZ: ' + jso['timezone'])
    print(f'''  {Fore.WHITE}║''')
    print(f'''  {Fore.WHITE}╚═{Fore.MAGENTA}[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE} Регион: ''' + jso['regionName'] + ' - ' + jso['zip'])
    print(f'''     {Fore.WHITE}║''')
    print(f'''     {Fore.WHITE}╚═{Fore.MAGENTA}[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE} Город: ''' + jso['city'])
    print()
elif parametros == '4':
    google()
# WARNING: Decompyle incomplete
