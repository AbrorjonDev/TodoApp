from django.urls import path
from .views import *

urlpatterns = [
    # path('', TodosList.as_view(), name='todos'),
    path('', TodosView.as_view(), name='todos'),
    path('new/',TodosCreate.as_view(), name='todo_create'),
    path('<slug:slug>/update/', TodosUpdateView.as_view(), name='todo_update'),
    path('<slug:slug>/delete/', TodosDeleteView.as_view(), name='todo_delete'),
    
]