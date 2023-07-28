from django.shortcuts import render
from .models import BlogPost

def index(request):
    # Fetch all published blog posts from the database
    posts = BlogPost.objects.filter(status='published').order_by('-pub_date')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)