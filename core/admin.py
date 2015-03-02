from django.contrib import admin
from models import *

# Register your models here.

class JournalAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'published', 'last_edited']
    search_fields = ['title']

admin.site.register(Journal, JournalAdmin)