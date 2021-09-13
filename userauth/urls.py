from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('profile/<int:duration>', views.profile, name="profile"),
    path('profile/add-training', views.addTraining, name="add-training"),
]
