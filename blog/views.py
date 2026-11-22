from typing import Any

from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView

from .models import Post


class PostListView(ListView):
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.order_by("-created_at")
        q = self.request.GET.get("q", "")
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset


class PostDetailView(DetailView):
    model = Post
