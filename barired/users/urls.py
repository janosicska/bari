from django.urls import path

from barired.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    user_list_view,
    user_follow,
)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("follow/", view=user_follow, name="user_follow"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
