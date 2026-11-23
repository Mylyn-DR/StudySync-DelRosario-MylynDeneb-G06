from django.db import models

# Create your models here.
class Goal(models.Model):      
    TYPE_CHOICES = [
        ("ROOM", "Room"),
        ("PERSONAL", "Personal")
    ] 
    name = models.CharField(max_length=255, null=false)
    desc = models.TextField()
    target_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    visibility = models.CharField(max_length=20, choices=TYPE_CHOICES, null=false)

class Milestone(models.Model): 
    

class TaskList(models.Model):


class Task(models.Model): 
    title = 
    desc = 
    type = #ROOM OR PERSONAL
    created_at = 
    updated_at