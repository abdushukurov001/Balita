from django.contrib import admin
from .models import Category, Tag, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at') 
    search_fields = ('name',)  

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'created_at')  
    list_filter = ('category', 'tags') 
    search_fields = ('title', 'description') 
    filter_horizontal = ('tags',) 

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'created_at') 
    search_fields = ('text',)  

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
