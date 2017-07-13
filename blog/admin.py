from django.contrib import admin

# Register your models here.

from .models import BlogAuthor, Blog, BlogComment


# Minimal registration of Models.
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)
admin.site.register(Blog)
