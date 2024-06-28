from django.urls import path

from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path("recipe/<int:_id>/", views.recipes, name="recipe"),
]
