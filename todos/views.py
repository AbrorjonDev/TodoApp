from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime
from .models import Todos
from .forms import TodosForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
class TodosList(ListView):
    model = Todos
    template_name = 'todos.html'
    context_object_name = 'todos'
    ordering = ['-deadline'] 

class TodosView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        todos = Todos.objects.filter(author_id=self.request.user.id).order_by('-deadline')
        for todo in todos:
            if todo.deadline > timezone.now():
                todo.status = 'missed'
            else:
                todo.status = 'not completed'
        context = {
            'todos':todos
        }
        return render(request, 'todos.html', context)

    def post(self, request, *args, **kwargs):
        form = TodosForm()
        form.instance.author = request.user
        form.save()
        return redirect("todos")
class TodosCreate(LoginRequiredMixin, CreateView):
    model = Todos
    template_name='todo_create.html'
    fields = ['todo', 'description', 'status', 'deadline']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

class TodosUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todos
    template_name = 'todo_update.html'
    fields = ['todo', 'description', 'status', 'deadline']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if todo.author == self.request.user:
            return True
        return False

class TodosDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todos
    # template_name = 'todo_delete.html'
    success_url = '/todos/'

    def test_func(self):
        todo = self.get_object()
        if todo.author == self.request.user:
            return True
        return False


    
