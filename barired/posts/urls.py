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
    path(
        route='add/',
        view=views.PostCreateView.as_view(),
        name='add'
    ),
    path(
        route='<slug:slug>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),

]
