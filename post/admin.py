from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Post, PostAdmin)