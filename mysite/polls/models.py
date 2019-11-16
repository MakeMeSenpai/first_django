#grabs time and date
import datetime
#takes from django db model classes in which our models will subclass
from django.db import models
#adjusts time and date based on time zone
from django.utils import timezone

# Create your models here.

#creates question's model
class Question(models.Model):
    #creates textbox for questions with a max character length of 200
    question_text = models.CharField(max_length=200)
    #creates a published date based on time of publish
    pub_date = models.DateTimeField('date published')
    #Found __str__ object therefor fixing questions
    def __str__(self):
        return self.question_text
    # #returns datetime of published queston
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #this prevents publish dates to be in the future and count as most recently posted
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 
    #adds attributes to our list objects and how they are displayed
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

#creates choice's model
class Choice(models.Model):
    #takes from questions model info on whether it exists, if not, cascade will delete it's 
    # following choices. ForeignKey tells Django that these choices are all part of the same 
    # question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #creates text box w/ max length of 200
    choice_text = models.CharField(max_length=200)
    #creates an interger box in which keeps track of votes made on each choice
    votes = models.IntegerField(default=0)
    #creates str object for our choices
    def __str__(self):
        return self.choice_text