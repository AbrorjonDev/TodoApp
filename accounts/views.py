from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login

# class UserRegisterView(UserRegisterForm, FormView):
#     model = User
#     form_class = UserRegisterForm()
#     template_name = 'signup.html'

#     def form_valid(self, form):
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         form.save()
#         user = authenticate(username=username, password=password)
#         login(self.request, user)
#         return super().form_valid(form)

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('todos')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form':form })

