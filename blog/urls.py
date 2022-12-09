from django.urls import path
from .views import *


urlpatterns = [
    path("", home_view, name="home"),
    path("posts/", posts_view, name="posts"),
    path('<slug:slug>/',post_detail,name='post_detail' ),
]