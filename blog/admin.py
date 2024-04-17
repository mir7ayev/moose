from django.contrib import admin
from .models import PostTags, Post, Comment

admin.site.register(PostTags)
admin.site.register(Post)
admin.site.register(Comment)
