# def get_zodiac_sign(month, day):
#     zodiac_signs = {
#         (12, 22): 'Козерог',
#         (1, 20): 'Водолей',
#         (2, 19): 'Рыбы',
#         (3, 21): 'Овен',
#         (4, 20): 'Телец',
#         (5, 21): 'Близнецы',
#         (6, 21): 'Рак',
#         (7, 23): 'Лев',
#         (8, 23): 'Дева',
#         (9, 23): 'Весы',
#         (10, 23): 'Скорпион',
#         (11, 22): 'Стрелец'
#     }
#
#     for key in zodiac_signs:
#         if (month == key[0] and day >= key[1]) or (month == key[0] + 1 and day < key[1]):
#             return zodiac_signs[key]
#
#
# month = 4
# day = 4
#
# zodiac_sign = get_zodiac_sign(month, day)
#
# print(f'Знак зодиака для дня {day} месяца {month}: {zodiac_sign}')
import requests

# def get_horoscope():
#     url = 'https://zodiac-signs.ru/api/aquarius/'
#     response = requests.get(url)
#     return response.json()
# print(get_horoscope())

url = 'https://ignio.com/r/export/utf/xml/daily/com.xml'
import requests
import xml.etree.ElementTree as ET


import requests
import xml.etree.ElementTree as ET

def get_horoscope(name_zodiac):
    url = 'http://img.ignio.com/r/export/utf/xml/daily/com.xml'
    response = requests.get(url)
    root = ET.fromstring(response.content)
    aries = root.find(name_zodiac)
    yesterday = aries.find('yesterday').text
    today = aries.find('today').text
    tomorrow = aries.find('tomorrow').text
    tomorrow02 = aries.find('tomorrow02').text
    horoscope = {
        'yesterday': yesterday.strip(),
        'today': today.strip(),
        'tomorrow': tomorrow.strip(),
        'tomorrow02': tomorrow02.strip(),
    }
    return horoscope
print(get_horoscope('aquarius'))

zodiac_list: dict = {

    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}

types_data = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}
