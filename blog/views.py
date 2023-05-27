import br as br
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .wikipedia_info import get_viki_info
from .data_info import actors, posts

# Create your views here.
import random

def main(request):
    # Выбираем случайные 3 поста
    random_posts = random.sample(posts, 3)

    # Передаем список случайных постов в контекст шаблона
    context = {
        'posts': random_posts
    }

    return render(request, 'blog/index.html', context)



def all_posts(request):
    return render(request, 'blog/posts.html')

def actor_list(request):

    context = {
        'actors': actors
    }
    return render(request, 'blog/actors.html', context)
def post_detail_actor(request, actor_name: str):
    actor = actors.get(actor_name)
    if actor is None:
        raise Http404('Актер не найден')
    info = get_viki_info(actor_name)
    context = {

        'actor': actor,
        'actor_photo': actor['actor_photo'],
        'info': info
    }
    return render(request, 'blog/actor.html', context)


def post_detail_name(request, name_post):
    context = {
        'name_post': name_post
    }
    if name_post.isdigit():
        return render(request, 'blog/detail_by_number.html', context)
    else:
        return render(request, 'blog/detail_by_name.html', context)

# def post_detail_number(request, number_post: int):
#     context = {
#         'number_post': number_post
#     }
#     return render(request, 'blog/detail_by_number.html', context)

def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnessworldrecords.html', context=context)