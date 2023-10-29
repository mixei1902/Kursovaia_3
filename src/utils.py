import json
import os
from datetime import datetime

# Определите путь к файлу внутри папки проекта
file_path = os.path.join(os.path.dirname(__file__), 'operations.json')

# Функция для загрузки данных из JSON-файла
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Функция для форматирования даты
def format_date(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime('%d.%m.%Y')

# Функция для маскировки номера карты и номера счета
def mask_card_and_account(data):
    if 'from' in data:
        data['from'] = f'{data["from"][:6]} XX** **** {data["from"][-4:]}'
    if 'to' in data:
        data['to'] = f'Счет **{data["to"][-4:]}'

# Основная функция для вывода списка операций
def show_recent_operations(data):
    # Фильтруем и сортируем данные по дате (последние операции сверху)
    recent_operations = sorted(
        [operation for operation in data if operation['state'] == 'EXECUTED'],
        key=lambda x: x['date'],
        reverse=True
    )[:5]

    for operation in recent_operations:
        mask_card_and_account(operation)  # Маскируем номер карты и счета
        formatted_date = format_date(operation['date'])
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        print(f"{formatted_date} {operation['description']}")
        if 'from' in operation and 'to' in operation:
            print(f"{operation['from']} -> {operation['to']}")
        print(f"{amount} {currency}")

if __name__ == '__main__':
    data = load_data(file_path)
    show_recent_operations(data)
