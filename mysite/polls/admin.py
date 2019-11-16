#original
# from django.contrib import admin

# #grabs from all models and imports our questions
# from .models import Question

# # Register your models here.

# # #registers our models
# # admin.site.register(Question)

#customized admin page
from django.contrib import admin
from .models import Question

#makes publish date come before question field, may not be impressive on a small scale, but 
# this is useful for large data organization
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# admin.site.register(Question, QuestionAdmin)

#this reorganizes the page, we add choice to .models and now make it admin available to create 
# choice. With (admin.StackedInline) this creates our choices, but its too expanded, so we shorten
# it with TabularInLine
class ChoiceInline(admin.TabularInline):     
    model = Choice
    #num of choices
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #django displays str by default. by doing this we create a list object
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #adds a side window for only showing questions according to the users preffered filter
    list_filter = ['pub_date']
    #this allows django to give us a search bar for all our questions
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)