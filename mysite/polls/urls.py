from django.urls import path
#this grabs from every file and imports views 
from . import views

#this is where are urls will be held
urlpatterns = [
    #this makes it so that an empty path (''), such as mysite/, sends us to the index view 
    path('', views.index, name="index"),
]
