from polls.models import Poll
from polls.models import Choice 
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    fieldsets = [        (None,                 {'fields': ['question']}), #show or hide information
       ('Date information',   {'fields': ['pub_date'] ,'classes':['collapse']}),
    ]
    list_display = ('question' , 'pub_date' , 'was_published_today')
    inlines = [ChoiceInline]
admin.site.register(Poll, PollAdmin)