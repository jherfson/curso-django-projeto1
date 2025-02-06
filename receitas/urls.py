from django.urls import path
from receitas.views import home
from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),

]