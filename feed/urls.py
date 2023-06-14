from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="feed-index-page"),
    path("addPost/",views.add_post,name="add-post-page"),
    path("post/<slug:slug>",views.post_detail,name="post-detail-page"),
    path("explore/",views.explore,name="explore-page"),

]
