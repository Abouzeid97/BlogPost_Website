from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.indexView.as_view(), name="index"),
    path("your_post", views.InputView.as_view(), name="new_post"),
    path("all_posts", views.all_postView.as_view(), name="all_posts"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("<slug:slug>", views.post_detailView.as_view(), name="post-detail"),
    
]
