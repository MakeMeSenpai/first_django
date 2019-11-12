#this grabs urls from djangos built in folders and builds our paths,
#include allows refferencing other URLconfs, chopping off the remaining url for further processing
from django.urls import include, path
#grabs contrib file from django and gives us an admins page
from django.contrib import admin
#this grabs from every file and imports views 
#from . import views

#this is where are urls will be held
urlpatterns = [
    #this makes it so that an empty path (''), such as mysite/, sends us to the index view 
    #path('', views.index, name="index"),
    #this sends us to the path mysite/polls/ by grabbing information from polls/urls.py
    path('polls/', include('polls.urls')),
    #this creates our admin page's path
    path('admin/', admin.site.urls),
]