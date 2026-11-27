from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.order_by("-created_at")
        q = self.request.GET.get("q", "")
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(body__icontains=q))
        return queryset


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"
    success_url = reverse_lazy("blog:post_list")
