from django.urls import path

from . import views

app_name = 'driverDatabase'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:driver_id>', views.driverDetail, name='driverDetail'),
]