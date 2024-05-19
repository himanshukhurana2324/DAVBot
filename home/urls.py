from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('run_script/', views.run_script, name='run_script'),
]