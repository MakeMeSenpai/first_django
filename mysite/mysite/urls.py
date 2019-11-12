"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#grabs contrib file from django and gives us an admins page
from django.contrib import admin
#this grabs urls from djangos built in folders and builds our paths,
#include allows refferencing other URLconfs, chopping off the remaining url for further processing
from django.urls import include, path

urlpatterns = [
    #this sends us to the path mysite/polls/ by grabbing information from polls/urls.py
    path('polls/', include('polls.urls')),
    #this creates our admin page's path
    path('admin/', admin.site.urls),
]
