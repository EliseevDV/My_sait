from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page_horoscope, name='start_page_horoscope'),
    path('type', views.type_list, name='type_list'),
    path('type/<type_zodiac>', views.type_info, name='type_info'),
    path('<int:sing_zodiac>', views.zodiac_info_int),
    path('<str:sing_zodiac>', views.zodiac_info, name='zodiac_info'),
    path('<int:month>/<int:day>', views.get_zodiac_sign, name='get_zodiac_sign'),

]
