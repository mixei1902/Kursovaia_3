import json
from datetime import datetime

# Загрузка данных из JSON-файла
with open('operations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# Функция для форматирования даты
def format_date(date_str):
    date = datetime.fromisoformat(date_str)  # Преобразование формата даты
    return date.strftime('%d.%m.%Y')


# Функция для маскировки номера карты
def mask_card(card_number):
    # Разделим номер карты на группы: первые 6 символов, последние 4 символа
    first_part = card_number[:6]
    last_part = card_number[-4:]

    # Замаскируем средние символы, если они есть
    middle_part = ' '.join(['*' * 4] * ((len(card_number) - 10) // 4))

    masked_card = f"{first_part} {middle_part} {last_part}"
    return masked_card


# Функция для маскировки номера счета
def mask_account(account_number):
    last_part = account_number[-4:]
    masked_account = f"**{last_part}"
    return masked_account


# Функция для вывода списка операций
def show_recent_operations(data):
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

        # Получение полного названия типа карты (если есть)
        card_type = operation["from"].split()[0] if "from" in operation else ""

        masked_from = mask_card(from_where) if from_where else ""
        masked_to = mask_account(to_where) if to_where else ""

        print(f"{date} {description}")
        if card_type:  # Если есть информация о типе карты
            print(f"{card_type} {masked_from} -> {masked_to}")
        else:
            print(f"Счет -> {masked_to}")
        print(f"{amount} {currency}")
        print()


# Вывод операций
show_recent_operations(data)
