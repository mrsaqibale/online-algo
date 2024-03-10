from automata import views 
from django.urls import path, include


urlpatterns = [
    path('', views.home),
    path('show/', views.show, name="show"),
]