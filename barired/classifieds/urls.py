# barired/classifieds/urls.py
from django.urls import path
from . import views


app_name = "classifieds"
urlpatterns = [
    path('', views.classified_list, name='classified_list'),
    path(
            route='add/',
            view=views.ClassifiedCreateView.as_view(),
            name='add'
        ),
    path(
        '<int:id>/<slug:slug>/',
        views.classified_detail,
        name='classified_detail'
    ),
    path(
        route='<int:id>/<slug:slug>/update/',
        view=views.ClassifiedUpdateView.as_view(),
        name='update'
    ),
]
