
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("post/<int:post_id>/", views.show_post, name="post"),
    path("add/", views.add_post, name="add"),
    path("login/", views.login, name="login"),
    path("contact/", views.contact, name="contact"),
    path("category/<int:category_id>/", views.show_category, name="category"),
]
