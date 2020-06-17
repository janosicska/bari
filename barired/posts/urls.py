# barired/posts/urls.py
from django.urls import path
from . import views


app_name = "posts"
urlpatterns = [
    path(
        route='',
        view=views.PostListView.as_view(),
        name='list'
    ),
]
