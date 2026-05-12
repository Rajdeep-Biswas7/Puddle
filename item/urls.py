from django.urls import path
from .import views
app_name = 'item'
urlpatterns = [
    path('new/', views.NewItem, name='new'),
    path('<int:pk>/', views.details, name='details'),
]