from django.urls import path
from . import views

app_name = 'Receipt'

urlpatterns = [
    path('', views.get_receipt, name='get_receipt'),

]
