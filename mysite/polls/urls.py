from django.urls import path
#this grabs from every file and imports views 
from . import views

#this is where are urls will be held
urlpatterns = [
    #this makes it so that an empty path (''), such as mysite/, sends us to the index view 
    path('', views.index, name="index"),
    #ex polls/5
    path('<int:question_id>/', views.detail, name="detail"),
    #ex polls/5/results/
    path('<int:question_id>/results/', views.results, name="results"),
    #ex polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name="vote"),
]
