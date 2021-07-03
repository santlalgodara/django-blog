from blog.models import Post
from django.shortcuts import get_object_or_404, render

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {
        'posts': posts
    })


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html',{
        'post': post,
        'categories': post.category.all(),
    })

