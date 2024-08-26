from django.urls import path
from . import views 

app_name = 'rapport'
urlpatterns = [
    path('',views.index,name = 'index'),
]