from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

data_week: dict = {
    'monday': 'Понедельник: Купить кофе',
    'tuesday': 'Вторник: Отвезти машину на СТО',
    'wednesday': 'Среда: Покупать автомобиль',
    'thursday': 'Четверг: Сходить в кино',
    'friday': 'Пятница: Учить английский',
    'saturday': 'Суббота: Учить Пайтон',
    'sunday': 'Воскресенье: Выходной',
}


# Create your views here.
def index_weeks(request) -> HttpResponse:
    return render(request, 'week_days/tasks_week.html', {'data': data_week})

def weeks_info(request, day_week: str) -> HttpResponse:
    discription_day_week = data_week[day_week]
    context = {
        'discription_day_week': discription_day_week,
        'day_week': day_week
    }
    return render(request, 'week_days/discripthions_task.html',context)



def count_day_week(reqvest, day_week: int) -> HttpResponse:
    day_week_list = list(data_week.keys())
    if day_week > len(day_week_list):
        return HttpResponseNotFound(f'<h2>Неверный номер дня - "{day_week}"</h2>')
    name_day_week = day_week_list[day_week - 1]
    name_day_path = reverse('weeks_info', args=[name_day_week])
    return HttpResponseRedirect(name_day_path)


people = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]
def people_list(request) -> HttpResponse:
    for person in people:
        print(person)

    context = {

        'people': people,
    }
    return render(request, 'week_days/people.html', context)
def people_info(request, people_detail) -> HttpResponse:

    context = {
        'people_detail': people_detail,

        'people': people,
    }
    return render(request, 'week_days/people_info.html', context)