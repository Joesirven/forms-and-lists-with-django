from django.urls import path
from posts.views import create_post, edit_post, posts_list, single_post

urlpatterns = [
    path("", posts_list, name="posts_list"),
    path("create/", create_post, name="create_post"),
    path("<int:id>/", single_post, name="single_post"),
    path("<int:id>/edit/", edit_post, name="edit_post"),
]
