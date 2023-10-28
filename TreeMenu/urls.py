from django.urls import path
from .views import TreeMenuViews

urlpatterns = [
    path('', TreeMenuViews.BaseMenu),
]
