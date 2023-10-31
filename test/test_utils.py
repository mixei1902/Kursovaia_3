import json
import pytest
from utils import format_date, mask_card, mask_account

# Загрузка данных из JSON-файла
with open('C:\Users\User\PycharmProjects\SkyEng\pythonProject\Kursovaia_3\src\operations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Тестирование функции format_date
def test_format_date():
    assert format_date("2023-10-31T12:34:56.789") == "31.10.2023"
    assert format_date("2019-04-04T23:20:05.206878") == "04.04.2019"
    assert format_date("2019-04-19T12:02:30.129240") == "19.04.2019"
    assert format_date("2019-07-13T18:51:29.313309") == "13.07.2019"

# Тестирование функции mask_card
def test_mask_card():
    assert mask_card("Tinkoff 1234567890123456") == "Tinkoff 1234 56** **** 3456"
    assert mask_card("Maestro 1308795367077170") == "Maestro 1308 79** **** 7170"
    assert mask_card("Мир 3766446452238784") == "Мир 3766 44** **** 8784"
    assert mask_card("Visa Classic 4062745111784804") == "Visa Classic 4062 27** **** 4804"

# Тестирование функции mask_account
def test_mask_account():
    assert mask_account("1234567890") == "Счёт **7890"
    assert mask_account("854580083267559933770") == "Счёт **3770"


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
