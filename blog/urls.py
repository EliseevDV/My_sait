from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/<actor_name>/', views.post_detail_actor, name='post_detail_actor'),
    # path('<int:number_post>/', views.post_detail_number, name='post_detail_number'),
    path('world_records/', views.get_guinness_world_records, name='get_guinness_world_records'),
    path('<slug:name_post>/', views.post_detail_name, name='post_detail_name'),
]
