from django.contrib import admin
from .models import Likes, Comment, Blog

admin.site.register(Likes)
admin.site.register(Comment)
admin.site.register(Blog)

