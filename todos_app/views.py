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

def add(request):
    return render(request, 'todos_app/edit.html')

def create(request):
    todo = Todo(title=request.POST['title'], deadline=request.POST['deadline'], percent_done=request.POST['percent_done'])
    todo.save()
    return redirect("/")

def edit(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'todos_app/edit.html', context)

def save(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.title = request.POST['title']
    todo.deadline = request.POST['deadline']
    todo.percent_done = request.POST['percent_done']
    todo.save()
    return redirect("/")

def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect("/")
