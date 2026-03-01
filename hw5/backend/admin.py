from django.contrib import admin

from .models import User, Post, Comment # type: ignore


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
