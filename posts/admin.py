from django.contrib import admin
from .models import Post, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('text', 'author__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_at')
    list_filter = ('author', 'post', 'created_at')
    search_fields = ('text', 'author__username', 'post__text')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_at')
    list_filter = ('user', 'post', 'created_at')
    search_fields = ('user__username', 'post__text')


