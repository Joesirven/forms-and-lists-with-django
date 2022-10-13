from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import PostForm

# Create your views here.
def posts_list(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_on")
    context = {
        "list_of_posts": posts,
    }
    return render(request, "posts/list.html", context)


def single_post(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post_object": post,
    }
    return render(request, "posts/detail.html", context)


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts_list")
    else:
        form = PostForm()
        context = {
            "post_form": form,
        }
        return render(request, "posts/create.html", context)


def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("single_post", id=id)
    else:
        form = PostForm(instance=post)
        context = {
            "post_object": post,
            "post_form": form,
        }
        return render(request, "posts/edit.html", context)
