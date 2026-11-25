from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

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


def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        body = request.POST.get("body", "")
        if title and body:
            Post.objects.create(title=title, body=body)
            return redirect("blog:post_list")
    return render(request, "blog/post_create.html")
