from django.contrib import admin
from .models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display=['title','timestamp','is_active','is_popular','total_votes',]
    list_filter = ['timestamp','is_active']
    fields = ['is_active', 'title']
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)

