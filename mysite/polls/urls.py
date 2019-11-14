# The Hard Way
# from django.urls import path
# #this grabs from every file and imports views 
# from . import views

# #this is where are urls will be held

# #tells Django witch app to grab the url from. useful for when your project contains multiple apps
# app_name = 'polls'
# urlpatterns = [
#     #this makes it so that an empty path (''), such as mysite/, sends us to the index view 
#     path('', views.index, name="index"),
#     #ex polls/5
#     path('<int:question_id>/', views.detail, name='detail'),
#     #ex polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     #ex polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

#The Easy way
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]