# barired/posts/urls.py
from django.urls import path
from . import views


app_name = "posts"
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(
        route='add/',
        view=views.PostCreateView.as_view(),
        name='add'
    ),
    path(
        '<int:id>/<slug:slug>/',
        views.post_detail,
        name='post_detail'
    ),
    path(
        route='<int:id>/<slug:post>/update/',
        view=views.PostUpdateView.as_view(),
        name='update'
    ),


]
