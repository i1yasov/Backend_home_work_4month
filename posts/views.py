from django.http.response import HttpResponse
from django.shortcuts import render

from posts.models import Post
from .models import Category
# Create your views here.


def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")


def about(request):
    return render(request, "about.html")


def me(request):
    return HttpResponse("<h1>ITS TEST!</h1>")


def post(request):
    posts = Post.objects.all()

    text = ""

    for post in posts:
        text += f"<h1>{post.title}</h1> <br> {post.content}<br>"

    return HttpResponse(text)

def category_list(request):
    categories = Category.objects.filter(is_active=True)

    return render(request, 'categories.html', {
    'categories': categories
})