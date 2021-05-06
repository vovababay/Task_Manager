from django.contrib import admin
from django.urls import path
from board.views import *

urlpatterns = [
    path('', home, name="home"),

]
