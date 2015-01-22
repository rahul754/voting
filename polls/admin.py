from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('Poll Question', {'fields':['question']}),
                 ('Date Information', {'fields':['pub_date']}),
                 ]
    list_display  = ['question','pub_date']
    search_fields = ['question']
    list_filter   = ['pub_date']
    inlines = [ChoiceInline]
    
admin.site.register(Poll, PollAdmin)
    