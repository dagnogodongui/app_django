from django.urls import path
from . import views 

app_name = 'teacher'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('add/',views.add,name = 'add'),
    path('edit/<int:id>/', views.edit, name='edit'),  # Notez le slash final ici
    path('delete/<int:id>/', views.delete, name='delete'),
]