
#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('count/',views.counts,name='count'),
    path('about/',views.about,name='about')
]
