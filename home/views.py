from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Category, About, Comment
from django.core.paginator import Paginator


def home_view(request):
    categories = Category.objects.all()
    main_obj = Post.objects.all()
    page_number = request.GET.get('page', 1)
    
    paginator = Paginator(categories, 1) 
    current_category = paginator.get_page(page_number)
    
    if current_category.object_list:
        posts = Post.objects.filter(category=current_category.object_list[0])
    else:
        posts = Post.objects.none()

    context = {
        'current_category': current_category,
        'posts': posts,
        'main_obj': main_obj,
        
    }
    
    return render(request, 'home.html', context)




def about_view(request):
    main_obj = Post.objects.all()
    about = About.objects.first()



    return render(request, 'about.html', context={
        'main_obj': main_obj,
        "about": about

    })


def contact_view(request):
    main_obj = Post.objects.all()


    return render(request, 'contact.html', context={
        'main_obj': main_obj
    })


def postDetail_view(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)  # Post mavjudligini tekshiramiz
        comments = Comment.objects.filter(post=post)
    except Post.DoesNotExist:
        return redirect('home')
    except Comment.DoesNotExist:  
        comments = None
    return render(request,'post-detail.html', context={
        'posts':post,
        'comments': comments
    } )
    

def category_view(request, id):
    try:
        categories = Category.objects.all()
        category = Category.objects.get(id=id)
        posts = Post.objects.filter(category=category)
        main_obj = Post.objects.all()
        page_number = request.GET.get('page', 1)
        
        paginator = Paginator(categories, 1) 
        current_category = paginator.get_page(page_number)
    
  

        return render(request, 'categories.html', context={
            'posts':posts,
            'category': category,
            'main_obj': main_obj,
            'current_category': current_category,

    })
    except Category.DoesNotExist:
        return redirect('home')
    


