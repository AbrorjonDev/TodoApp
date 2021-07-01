from django.contrib import admin
from .models import Todos

class TodosAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('todo',)}
    list_display = ['todo', 'author', 'publish_date', 'deadline', 'status']
    list_filter = ['status']
    
admin.site.register(Todos, TodosAdmin)
