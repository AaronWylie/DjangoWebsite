from django.urls import path
from . import views


urlpatterns = [
    path('<str:pk_test>/', views.plants),

]

