from automata import views 
from django.urls import path, include


urlpatterns = [
    path('', views.test),
]