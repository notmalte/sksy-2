from django.http import HttpResponse
from django.shortcuts import render

from .models import Todo


def index(request):
    todos_list = Todo.objects.all()
    context = {
        'todos_list': todos_list,
    }
    return render(request, 'todos_app/index.html', context)
