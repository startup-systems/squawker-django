from django.contrib import admin
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_text', 'post_date']

admin.site.register(Post, PostAdmin)
