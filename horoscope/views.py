from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from . import Get_horoscope

# Create your views here.
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

def index(request) -> HttpResponse:
    return render(request, 'my_page/main_page.html')

def start_page_horoscope(request) -> HttpResponse:
    context = {
        'zodiac_list': zodiac_list
    }
    return render(request, 'horoscope/horoscope_start_page.html', context)


def zodiac_info(request, sing_zodiac: str) -> HttpResponse:
    zodiac_discript = Get_horoscope.get_horoscope(sing_zodiac)
    info = zodiac_list.get(sing_zodiac)

    context = {
        'zodiac_list': zodiac_list,
        'info': info,
        'zodiac_discript': zodiac_discript,
        'sing_zodiac': sing_zodiac,

    }
    return render(request, 'horoscope/info_zodiac.html', context)



def zodiac_info_int(request, sing_zodiac: int) -> HttpResponse:
    list_zodiac = list(zodiac_list.keys())
    if sing_zodiac > len(list_zodiac):
        return HttpResponseNotFound(f'<h2>Не правильный порядковый номер - "{sing_zodiac}"</h2>')
    name_zodiac = list_zodiac[sing_zodiac - 1]
    zodiac_path = reverse('zodiac_info', args=[name_zodiac])
    return HttpResponseRedirect(zodiac_path)


def type_info(request, type_zodiac: str) -> HttpResponse:
    zodiac_menu = list(types_data.keys())
    if type_zodiac in zodiac_menu:
        li_elements = ''
        for type in types_data[type_zodiac]:
            zodiac_path = reverse('zodiac_info', args=[type])
            li_elements += f"""
            <li><a href='{zodiac_path}'>{type.title()}</a></li>
            """
        response = f"""
        <ol>
        {li_elements}
        </ol>"""
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f'<h2>Такого знака зодиака "{type_zodiac}" не существует</h2>')

def type_list(request) -> HttpResponse:
    context = {
        'types_data': types_data
    }
    return render(request, 'horoscope/type_horoscope.html', context)


def get_zodiac_sign(request, month, day):
    zodiac_signs = {
        (12, 22): 'capricorn',
        (1, 20): 'aquarius',
        (2, 19): 'pisces',
        (3, 21): 'aries',
        (4, 21): 'taurus',
        (5, 21): 'gemini',
        (6, 21): 'cancer',
        (7, 22): 'leo',
        (8, 21): 'virgo',
        (9, 23): 'libra',
        (10, 23): 'scorpio',
        (11, 22): 'sagittarius',
    }

    for key in zodiac_signs:
        if (month == key[0] and day >= key[1]) or (month == key[0] + 1 and day < key[1]):
            zodiac_path = reverse('zodiac_info', args=[zodiac_signs[key]])
            response = f"Ваш знак зодиака <li><a href='{zodiac_path}'>{zodiac_signs[key].title()}</a></li>"
            return HttpResponse(response)
def beautiful_table(request):
    return render(request, 'horoscope/beautiful_table.html')