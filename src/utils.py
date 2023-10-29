import json
from datetime import datetime

# Загрузка данных из JSON-файла
with open('operations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def format_date(date_str):
    '''Функция для форматирования даты'''
    date = datetime.fromisoformat(date_str)
    return date.strftime('%d.%m.%Y')


def mask_card(card_number):
    '''Функция для маскировки номера карты'''
    last_part = card_number[-4:]
    first_part = card_number[:len(card_number)-12]
    middle_part = card_number[-12:-10]
    masked_card = f"{first_part} {middle_part}** **** {last_part}"
    return masked_card

def mask_account(account_number):
    '''Функция для маскировки номера счета'''
    last_part = account_number[-4:]
    masked_account = f"Счёт **{last_part}"
    return masked_account

def show_recent_operations(data):
    '''Функция для вывода списка операций и сортировка 5 послених успешных операций'''
    executed_operations = [op for op in data if op.get('state') == "EXECUTED"]
    sorted_operations = sorted(executed_operations, key=lambda x: x["date"], reverse=True)
    recent_operations = sorted_operations[:5]

    for operation in recent_operations:
        date = format_date(operation["date"])
        description = operation["description"]
        from_where = operation.get("from", "")
        to_where = operation.get("to", "")
        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]["name"]

        masked_from = mask_card(from_where) if from_where else ""
        masked_to = mask_account(to_where) if to_where else ""

        print(f"{date} {description}")
        print(f"{masked_from} -> {masked_to}")
        # print(f"Счет -> {masked_to}")
        print(f"{amount} {currency}")
        print()


# Вывод операций
show_recent_operations(data)
