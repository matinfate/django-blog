from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("",views.post_list, name="post_list"),
    path("<int:pk>",views.PostDetailView.as_view(), name="post_detail"),
]
