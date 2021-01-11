from django.urls import path
from .views import *
app_name='search'
urlpatterns = [
    path('',youtube_search,name='youtube_search')
]