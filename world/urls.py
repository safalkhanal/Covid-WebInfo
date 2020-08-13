from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #path('<slug:country_name>', views.country),
    path('test', views.test),
    path('<slug:country_code>/', views.country)
]