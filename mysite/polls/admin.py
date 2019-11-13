from django.contrib import admin

#grabs from all models and imports our questions
from .models import Question

# Register your models here.

#registers our models
admin.site.register(Question)