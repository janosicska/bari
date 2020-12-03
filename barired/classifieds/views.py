from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.shortcuts import (render, get_object_or_404)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from .models import Classified


@login_required
def classified_list(request):
    classifieds = Classified.objects.all()

    return render(request,
                  'classifieds/classified_list.html',
                  {'classifieds': classifieds})


@login_required
def classified_detail(request, id, slug):
    classified = get_object_or_404(Classified, id=id, slug=slug)

    return render(request,
                  'classifieds/classified_detail.html',
                  {'classified': classified,
                   })


class ClassifiedCreateView(LoginRequiredMixin, CreateView):
    model = Classified
    fields = [
        'title',
        'photo',
        'price',
        'category',
        'description',
    ]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ClassifiedUpdateView(LoginRequiredMixin, UpdateView):
    model = Classified
    fields = [
        'title',
        'photo',
        'price',
        'category',
        'description',
    ]
    action = "Update"
