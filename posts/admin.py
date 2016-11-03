from django.contrib import admin
from posts.models import Post
# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", "updated", "timestamp")

    class Meta:
        model = Post
admin.site.register(Post)
