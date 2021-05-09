# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)
    # retona informação sobre o name
    def __str__(self):
        return self.name

class Item(models.Model):
    ## os itens farão parte do ToDoList
    ## Se ToDoList for deletado, os itens também serão. 
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # informações do item
    text = models.CharField(max_length=300)
    # se a todolist está completa ou não
    complete = models.BooleanField()

    def __str__(self):
        return self.text