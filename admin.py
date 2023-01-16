from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('Title',)
    ordering = ['Title',]
    list_filter = ( 'Title',)
    search_fields = ('Title',)

admin.site.register(Question,QuestionAdmin)

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('Title','html','MinAns','MaxAns')
    ordering = ['Title','MinAns','MaxAns']
    list_filter = ( 'Title','MinAns','MaxAns')
    search_fields = ('Title','MinAns','MaxAns')

admin.site.register(Template,TemplateAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('Title','question','position','template','SecAfter')
    ordering = ['Title','position','question']
    list_filter = ( 'Title','position','question')
    search_fields = ('Title','position','question')

admin.site.register(Event,EventAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer','event','EntryAgent')
    ordering = ['answer','event','EntryAgent']
    list_filter = ( 'answer','event','EntryAgent')
    search_fields = ('answer','event','EntryAgent')

admin.site.register(Answer,AnswerAdmin)
