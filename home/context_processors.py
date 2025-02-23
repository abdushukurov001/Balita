from django.db.models import Count
from .models import Category, Tag, Post



def category_processor(request):
    categories = Category.objects.annotate(post_count=Count('posts'))
    unique_tags = Tag.objects.all()
    posts = Post.objects.all().order_by('-id')
    count_obj = Category.objects.annotate(post_count=Count('posts'))
    print(posts.count())
    return {
            'categories': categories, 
            'count_obj': count_obj, 
            'unique_tags': unique_tags ,
            'posts': posts
            }                