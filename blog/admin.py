from django.contrib import admin
from .models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'author')
    raw_id_fields = ('tags', 'likes')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    raw_id_fields = ('posts',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post',)
    raw_id_fields = ('post', 'author')
