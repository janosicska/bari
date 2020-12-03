from django.views.generic import ListView, DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.shortcuts import (render, get_object_or_404)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Post

from .forms import CommentForm


@login_required
def post_detail(request, id, slug):
    post = get_object_or_404(Post, slug=slug, id=id)

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  'posts/post_detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   })


@login_required
def post_list(request):
    posts = Post.objects.all()

    return render(request,
                  'posts/post_list.html',
                  {'posts': posts})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'name',
        'photo',
        'description',
    ]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = [
        'name',
        'photo',
        'description',
    ]
    action = "Update"


# class PostListView(LoginRequiredMixin, ListView):
#     model = Post
#     context_object_name = 'posts'


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, )
    sent = False

    # if request.method == 'POST':
    #     # Form was submitted
    #     form = EmailPostForm(request.POST)
    #     if form.is_valid():
    #         # Form fields passed validation
    #         cd = form.cleaned_data
    #         post_url = request.build_absolute_uri(post.get_absolute_url())
    #         subject = f"{cd['name']} recommends you read {post.title}"
    #         message = f"Read {post.title} at {post_url}\n\n" \
    #                   f"{cd['name']}\'s comments: {cd['comments']}"
    #         send_mail(subject, message, 'admin@myblog.com', [cd['to']])
    #         sent = True
    #
    # else:
    #     form = EmailPostForm()
    # return render(request, 'blog/post/share.html', {'post': post,
    #                                                 'form': form,
    #                                                 'sent': sent})
