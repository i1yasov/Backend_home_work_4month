from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from posts.models import Post
from .models import Category
from .forms import PostForm, CategoryForm
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

def get_posts(request):
    posts = Post.objects.all()

    return render(request, "posts/post_list.html", context={"posts": posts})


def get_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "posts/post_detail.html", context={"post": post})
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("posts")

    else:
        form = PostForm()

    return render(
        request,
        "posts/post_create.html",
        {"form": form}
    )


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("posts")

    else:
        form = CategoryForm()

    return render(
        request,
        "posts/category_create.html",
        {"form": form}
    )