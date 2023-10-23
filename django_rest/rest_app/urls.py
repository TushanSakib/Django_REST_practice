from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('student/',StudentAPI.as_view()),
    #path('',home),
    #path('student/',post_student),
    #path('update_student/<id>',update_student),
    #path('delete_student/<id>',delete_student),
    path('get_book/',get_book),
]