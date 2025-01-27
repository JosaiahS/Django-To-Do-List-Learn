from django.db import models
#Prebuilt djando models
from django.contrib.auth.models import User
#For database structures

class Task(models.Model):
    #One to many relationship
    #What is a form?
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #Meant for simple values
    title = models.CharField(max_length=200)
    #More complex text
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']

