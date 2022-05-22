from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imprint', views.imprint),
    path('add', views.add),
    path('create', views.create),
    path('edit/<int:todo_id>', views.edit),
    path('save/<int:todo_id>', views.save),
    path('delete/<int:todo_id>', views.delete),
]
