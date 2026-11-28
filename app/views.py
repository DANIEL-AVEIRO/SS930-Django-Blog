from django.shortcuts import render, redirect
from app.models import PostModel, CategoryModel

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
        if post.image:
            post.image.delete()
        post.delete()
        return redirect("post_list")


def post_details(request):
    return render(request, "post_details.html")


def category_create(request):
    if request.method == "GET":
        return render(request, "category_create.html")
    if request.method == "POST":
        name = request.POST.get("name")

        category = CategoryModel.objects.create(
            name=name,
        )
        category.save()
        return redirect("category_list")


def category_list(request):
    categories = CategoryModel.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "category_list.html", context)


def category_update(request, pk):
    category = CategoryModel.objects.get(id=pk)
    if request.method == "GET":
        context = {
            "category": category,
        }
        return render(request, "category_update.html", context)
    if request.method == "POST":
        name = request.POST.get("name")

        category.name = name
        category.save()
        return redirect("category_list")


def category_delete(request, pk):
    category = CategoryModel.objects.get(id=pk)
    if request.method == "GET":
        context = {
            "category": category,
        }
        return render(request, "category_delete.html", context)
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
