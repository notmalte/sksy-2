from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Todo


def index(request):
    todos_list = Todo.objects.all()
    context = {
        'todos_list': todos_list,
    }
    return render(request, 'todos_app/index.html', context)


def imprint(request):
    return render(request, 'todos_app/imprint.html')
