from django.shortcuts import render, redirect
from app.models import PostModel

# Create your views here.


def index(request):
    posts = PostModel.objects.all().order_by("-created_at")
    content = {
        "posts": posts,
    }
    return render(request, "index.html", content)


def post_create(request):
    if request.method == "GET":
        return render(request, "post_create.html")
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        post = PostModel.objects.create(
            title=title,
            content=content,
            image=image,
        )
        post.save()
        return redirect("post_list")


def post_list(request):
    posts = PostModel.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "post_list.html", context)


def post_update(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == "GET":
        context = {
            "post": post,
        }
        return render(request, "post_update.html", context)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        post.title = title
        post.content = content
        if image:
            if post.image:
                post.image.delete()
            post.image = image
        post.save()
        return redirect("post_list")


def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == "GET":
        context = {
            "post": post,
        }
        return render(request, "post_delete.html", context)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")


def post_details(request):
    return render(request, "post_details.html")
