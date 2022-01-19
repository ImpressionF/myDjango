from django.urls import path

from apps.second import views

urlpatterns = [
    path('second/', views.goSecond)
]
