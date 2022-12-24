
from django.db import models
class TodoListItem(models.Model):
    '''
    id: added by default by django
    conent: user defined
    
    TodolistItem.objects.filter(gender='male'), 10, 20, 30
    '''
     
    content = models.TextField() 

