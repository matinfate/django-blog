from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("new/", views.post_create, name="post_create"),
    path("<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
]
