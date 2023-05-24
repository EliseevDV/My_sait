from django.urls import path
from .views import get_rectangle_area_str, get_square_area_str, get_circle_area_str, get_rectangle_area_int, \
    get_square_area_int, get_circle_area_int, index_geometry

urlpatterns = [
    path('', index_geometry, name='geometry_start_page'),
    path('get_rectangle_area/<int:width>/<int:height>', get_rectangle_area_int),
    path('get_square_area/<int:width>', get_square_area_int),
    path('get_circle_area/<int:radius>', get_circle_area_int),
    path('rectangle/<int:width>/<int:height>', get_rectangle_area_str, name='rectangle'),
    path('square/<int:width>', get_square_area_str, name='square'),
    path('circle/<int:radius>', get_circle_area_str, name='circle'),

]
