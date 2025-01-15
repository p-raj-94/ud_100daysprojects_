from django.contrib import admin
from .models import TodoList, Task


class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ['name']

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','todolist','created_at', 'due_date', 'completed')
    search_fields = ['name']

# Register your models here.
admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Task, TaskAdmin)
