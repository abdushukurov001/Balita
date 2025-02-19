from django.db.models import Count
from .models import Category, Tag



def category_processor(request):
    categories = Category.objects.annotate(post_count=Count('posts'))
    unique_tags = Tag.objects.all()

    count_obj = Category.objects.annotate(post_count=Count('posts'))

    return {
            'categories': categories, 
            'count_obj': count_obj, 
            'unique_tags': unique_tags 
            }                