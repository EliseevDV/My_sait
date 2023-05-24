from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_weeks, name='index_weeks'),
    path('people/', views.people_list, name='people'),
    path('people/<str:people_detail>', views.people_info, name='people_info'),

    path('<int:day_week>/', views.count_day_week),
    path('<str:day_week>/', views.weeks_info, name='weeks_info'),

]
