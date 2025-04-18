from django.contrib import admin

# Register your models here.
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'points')  # что будет видно в списке
