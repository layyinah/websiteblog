from django.contrib import admin
from.models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'img', 'auth', 'date']
admin.site.register(Blog,BlogAdmin)