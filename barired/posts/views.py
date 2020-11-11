from django.views.generic import ListView, DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'name',
        'description',
    ]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = [
        'name',
        'description',
    ]
    action = "Update"
