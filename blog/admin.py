from django.contrib import admin

# Register your models here.

from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):

    list_display = ('full_name','age')

admin.site.register(Blog, BlogAdmin)