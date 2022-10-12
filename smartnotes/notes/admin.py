from django.contrib import admin

# Register your models here.
from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(models.Note, NotesAdmin)