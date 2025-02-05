
# Python obfuscation by freecodingtools.org
                    
from fake_useragent import UserAgent
import requests
import random
from termcolor import colored
import string
import time

number = '+79999999999'

# Учетные записи
senders = {
    'raumonatuhadi@mail.ru': 'a7r6U9J6KHDaguAsidDH',
    'floworadpewoodvi@mail.ru': 'ZcyUg5MUq8jMr9i8aST1',
    'letzegebquirdisnui@mail.ru': 'abniAcbrCjRskpysMc75',
    'millveramontmoni@mail.ru': 'bLd8Zg4tqfxmUq7KW5jW',
    'letkixipromnussi@mail.ru': 'bNraxddiagE9Sx23SxYt',
    'hotriosmartraverba@mail.ru': 'cALqh0bjnPefyiu7WL0v',
    'pillgemisscritcomsa@mail.ru': 'dHBUrMg6aqXhvx0m1cVf',
    'leigedeamvebig@mail.ru': 'dVTsGqDbZYbjse9iHNR2',
    'knocrufridunringgent@mail.ru': 'dn333DbbuEfGnqw08Rxm',
    'tworensodiapansaa@mail.ru': 'dsGajJE1TtiAGgZsgyvQ',
    'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
    'terbgebuoviror@mail.ru': 'gaqaKs06xg22kkXXW2LU',
    'tioreibunthandvahear@mail.ru': 'ggKygTjxSLzwm4tWd43B',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
    'aria.therese.svensson@mail.com': 'Zorro1ab',
    'taterbug@verizon.net': 'Holly1!',
    'ejbrickner@comcast.net': 'Pass1178',
    'teressapeart@cox.net': 'Quinton2329!',
    'liznees@verizon.net': 'Dancer008',
    'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
    'kcdg@charter.net': 'Jennifer3*',
    'bean_118@hotmail.com': 'Liverpool118!',
    'dsdhjas@mail.com': 'LONGHACH123',
    'robitwins@comcast.net': 'May241996',
    'wasina@live.com': 'Marlas21',
    'aruzhan.01@mail.com': '1234567!',
    'rob.tackett@live.com': 'metallic',
    'lindahallenbeck@verizon.net': 'Anakin@2014',
    'hlaw82@mail.com': 'Snoopy37$$',
    'paintmadman@comcast.net': 'mycat2200*',
    'prideandjoy@verizon.net': 'Ihatejen12',
    'sdgdfg56@mail.com': 'kenwood4201',
    'garrett.danelz@comcast.net': 'N11golfer!',
    'gillian_1211@hotmail.com': 'Gilloveu1211',
    'sunpit16@hotmail.com': 'Putter34!',
    'fdshelor@verizon.net': 'Masco123*',
    'yeags1@cox.net': 'Zoomom1965!',
    'amine002@usa.com': 'iScrRoXAei123',
    'bbarcelo16@cox.net': 'Bsb161089$$',
    'laliebert@hotmail.com': 'pirates2',
    'vallen285@comcast.net': 'Delft285!1!',
    'sierra12@email.com': 'tegen1111',
    'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
    'kmay@windstream.net': 'Nascar98',
    'redbrick1@mail.com': 'Redbrick11',
    'ivv9ah7f@mail.com': 'K226nw8duwg',
    'erkobir@live.com': 'floydLAWTON019',
    'Misscarter@mail.com': 'ashtray19',
    'carlieruby10@cox.net': 'Lollypop789$',
    'blackops2013@mail.com': 'amason123566',
    'caroline_cullum@comcast.net': 'carter14',
    'dpb13@live.com': 'Ic&ynum13',
    'heirhunter@usa.com': 'Noguys@714',
    'sherri.edwards@verizon.net': 'Dreaming123#',
    'rami.rami1980@hotmail.com': 'ramirami1980',
    'jmsingleton2@comcast.net': '151728Jn$$',
    'aberancho@aol.com': '10diegguuss10',
    'dgidel@iowatelecom.net': 'Buster48',
    'gpopandopul@mail.com': 'GEORG62A',
    'bolgodonsk@mail.com': '012345678!',
    'colbycolb@cox.net': 'Signals@1',
    'nicrey4@comcast.net': 'Dabears54',
    'mordechai@mail.com': 'Mordechai',
    'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
    'tarabedford@comcast.net': 'Money4me',
    'mycockneedsit@mail.com': 'benjamin3',
    'saralaine@mail.com': 'sarlaine12!1',
    'jonb2006@verizon.net': '1969Camaro',
    'rjhssa1@verizon.net': 'Donna613*',
    'cameron.doug@charter.net': 'Jake2122$',
    'bridget.shappell@comcast.net': 'Brennan1',
    'rugs8@comcast.net': 'baseball46',
    'averyjacobs3@mail.com': '1960682644!',
    'lstefanick@hotmail.com': 'Luv2dance2',
    'bchavez123@mail.com': 'aadrianachavez',
    'lukejamesjones@mail.com': 'tinkerbell1',
    'emahoney123@comcast.net': 'Shieknmme3#',
    'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
    'jet747@cox.net': 'Sadie@1234',
    'landsgascareservices@mail.com': 'Alisha25@',
    'samantha224@mail.com': 'Madden098!@',
    'kbhamil@wowway.com': 'Carol1940',
    'email@bjasper.com': 'Lhsnh4us123!',
    'biggsbrian@cox.net': 'Trains@2247Trains@2247',
    'dzzeblnd@aol.com': 'Geosgal@1',
    'jtrego@indy.rr.com': 'Jackwill14!',
    'chrisphonte.rj@comcast.net': 'Junior@3311',
    'tvwifiguy@comcast.net': 'Bill#0101',
    'defenestrador@mail.com': 'm0rb1d8ss',
    'glangley@gmx.com': 'ironhide',
    'charlotte2850@hotmail.com': 'kelalu2850'
}


def generate_phone_number():
    country_codes = ['+7', '+380', '+375']
    country_code = random.choice(country_codes)
    phone_number = ''.join(random.choices('0123456789', k=10))
    formatted_phone_number = f'{country_code}{phone_number}'
    return formatted_phone_number

def generate_random_email():
    return random.choice(list(senders.keys()))

def send_complaint(username, telegram_id, number, email, repeats, complaint_choice):
    url = 'https://telegram.org/support'
    user_agent = UserAgent().random
    headers = {
        'User-Agent': user_agent,
        'Authorization': f'Bearer {senders[email]}'
    }
    complaints_sent = 0

    complaint_texts = {
        "1": f'Добрый день поддержка Telegram! Аккаунт {username}, {telegram_id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться. Прошу разберитесь с этим. Заранее спасибо!',
        "2": f'Аккаунт {username}, {telegram_id} приобрёл премиум в вашем сервисе чтобы обходить наказания за спам и совершает спам-рассылки в личные сообщения пользователям и в чаты. Прошу проверить информацию!',
        "3": f"Здравствуйте. Аккаунт {username}, id {telegram_id} оскорбляет меня и мою маму. Мне это очень не приятно, поэтому и пишу вам. Огромная просьба разобраться и заблокировать данного пользователя, так как это нарушает политику сервиса. Благодарю",
        "4": f"Здравствуйте. Аккаунт {username}, id {telegram_id}. Очень много и часто нарушает политику сервиса Телеграм. А именно, оскорбляет, сливает личные данные пользователей, продает различные услуги. Прошу разобраться и наказать данный аккаунт.",
        "5": f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {username}, а мой айди, если злоумышленник поменял юзернейм —  {telegram_id}. Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных.",
        "6": f"Здравствуйте, сидя на просторах сети Телеграм, я заметил пользователя, который совершает спам-рассылки. Мне и другим пользователям это очень не нравится. Его аккаунт: {username}, ID {telegram_id}. Огромная просьба разобраться с этим и заблокировать данного пользователя. Заранее спасибо.",
        "7": f"Сидя на просторах Телеграм, заметил пользователя, который продает услуги деанона и лжеминирования. Ссылка на канал и юзер админа: {username}, id админа: {telegram_id}. Большая просьба заблокировать канал и пользователя, так как это нарушает политику сервиса.",
        "8": f"На сервисе Телеграм обнаружил пользователя, который накручивает на канал реакции, подписки и просмотры. Ссылка на посты с накруткой и аккаунт администратора: {username}, id администратора на случай, если поменяет юзернейм: {telegram_id}. Прошу разобраться и заблокировать пользователя, так как это нарушает правила Телеграм."
    }

    text = complaint_texts.get(complaint_choice, "Некорректный выбор жалобы")
    payload = {'text': text, 'number': number, 'email': email}

    print(colored("Начинается отправка жалоб с следующими данными:", "green"))
    print(colored(f"URL: {url}", "green"))
    print(colored(f"Payload: {payload}", "green"))

    try:
        for i in range(int(repeats)):
            print(colored(f"\nШаг {i + 1}/{repeats}: Отправка жалобы...", "green"))
            try:
                response = requests.post(url, headers=headers, data=payload, timeout=10)
                print(colored(f"Статус код ответа: {response.status_code}", "green"))
                if response.status_code == 200:
                    print(colored(f"✔️ Жалоба {i + 1} успешно отправлена!", 'green'))
                    print(colored(f"Отправлено от: {email} | Номер: {number}", 'green'))
                else:
                    print(colored(f"❌ Не удалось отправить жалобу {i + 1}. Код статуса: {response.status_code}", 'red'))
                    print(colored(f"Тело ответа: {response.text}", 'red'))
            except requests.RequestException as e:
                print(colored(f"Ошибка отправки жалобы {i + 1}: {str(e)}", 'red'))
            # Добавляем небольшую паузу между отправками для снижения нагрузки
            time.sleep(1)
    except Exception as e:
        print(colored(f"Произошла ошибка при обработке запросов: {str(e)}", 'red'))

from termcolor import colored
from termcolor import colored

def display_banner_and_menu():
    combined_output = """
            ⣿⠲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⡏⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⡰⠋⢙⣿⣦
⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣦⣮⣤⡀⣸⣿⣿ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⣿⢟⠟ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ[1] Virtual Number ㅤㅤㅤㅤㅤㅤㅤㅤ                                                               
⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣷⣷⣿⡁ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ[2] Permiumㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ                                                                      
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢸⣿⣿⣧⣿⣿⣆⡀ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ[3] Insult (Tohin)
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣤⣿⣿⣿⡟⠹⣿⡀ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ[4] Breaking the rules
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣴⣿⢧ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ[5] Sessions (jalasat) 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⣿⣿⣿⣿⣿⣿⣿⡀ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ[6] Spam (Harznameh)
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣸⣿⣿⣿⣿⣿⣿⣿⢳ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ[7] Sale                          
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢀⣿⣿⣿⣿⣿⣿⣿⣿⡇ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ[8] Cheat (copy right)
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣼⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⇇
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠛⠻⠿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⣿⣿⠏⠀BarDia DarZaN @The_EmPloYeR 
برای اجرای  سورس فیلترشکنتون باید روشن باشه.               """
    print(colored(combined_output, "red"))

def complaint():
    complaint_choice = input("Put The Number: ")
    
    if complaint_choice in ["1", "2", "3", "4", "6", "7", "8"]:
        username = input("Put Telegram Username (https://t.me/username): ")
        telegram_id = input("Telegram numeric ID(tg://openmessage?user_id=(numeric ID):  ")
        repeats = int(input("Enter the number of reports: "))

        for _ in range(repeats):
            number = generate_phone_number()
            email = generate_random_email()
            send_complaint(username, telegram_id, number, email, repeats, complaint_choice)
    else:
        print(colored("Incorrect number! Try again.", 'red'))

# Вызов функций
display_banner_and_menu()
complaint()