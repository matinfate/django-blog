from django.shortcuts import render
from django.views.generic import DetailView

from .models import Post


def post_list(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


class PostDetailView(DetailView):
    model = Post
