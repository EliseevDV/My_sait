from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index_geometry(request):
    return render(request, 'geometry/index_geometry.html')
# ----------------------------------------------------------------------------------------------------------------------

# Функции для редиректа на страницы, где будет выведен результат вычислений
def get_rectangle_area_int(request, width: int, height: int) -> HttpResponseRedirect:
    url = reverse('rectangle', args=[width, height])
    return HttpResponseRedirect(url)


def get_square_area_int(request, width: int) -> HttpResponseRedirect:
    url = reverse('square', args=[width])
    return HttpResponseRedirect(url)


def get_circle_area_int(request, radius: int) -> HttpResponseRedirect:
    url = reverse('circle', args=[radius])
    return HttpResponseRedirect(url)


# -------------------------------------------------------------------------------------------------------------------------
# Функции для вывода результата вычислений на странице
def get_rectangle_area_str(request, width: int, height: int) -> HttpResponse:
    html = f"""
        <h2>Площадь прямоугольника размером {width}x{height} равна {width * height}</h2>
    """

    return HttpResponse(html)


def get_square_area_str(request, width) -> HttpResponse:
    html = f"""
        <h2>Площадь квадрата размером {width}x{width} равна {width * width}</h2>
    """
    return HttpResponse(html)


def get_circle_area_str(request, radius) -> HttpResponse:
    html = f"""
        <h2>Площадь круга радиуса {radius} равна {3.14 * radius ** 2}</h2>
    """
    return HttpResponse(html)

# -------------------------------------------------------------------------------------------------------------------------
