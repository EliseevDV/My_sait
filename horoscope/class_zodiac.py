from datetime import datetime, timedelta
from typing import Tuple
class Zodiac:
    def __init__(self):
        self.zodiac_list = {
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

    def get_dates(self, sign):
        info = self.zodiac_list.get(sign.lower())
        if info:
            dates = info.split('(')[-1].split(')')[0]
            return dates
        else:
            return "Знак зодиака не найден."

    def get_name(self, sign):
        info = self.zodiac_list.get(sign.lower())
        if info:
            name = info.split(' - ')[0]
            return name
        else:
            return "Знак зодиака не найден."

    def get_description(self, sign):
        info = self.zodiac_list.get(sign.lower())
        if info:
            description = info.split(' - ')[1].split('(')[0].strip()
            return description
        else:
            return "Знак зодиака не найден."
zodiac = Zodiac()

sign = 'capricorn'
print(f"Даты: {zodiac.get_dates(sign)}")
print(f"Название: {zodiac.get_name(sign)}")
print(f"Описание: {zodiac.get_description(sign)}")



