from django.views.generic import ListView, DetailView
from django.views.generic import CreateView

from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = [
        'name',
        'description',
        'type',
    ]
