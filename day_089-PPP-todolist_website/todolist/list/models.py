from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name