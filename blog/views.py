from django.views.generic import DetailView, ListView

from .models import Post


class PostListView(ListView):
    queryset = Post.objects.order_by("-created_at")
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
