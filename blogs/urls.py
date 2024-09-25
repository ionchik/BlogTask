from django.urls import path
from .views import home, create_post, edit_post

app_name = 'blogs'
urlpatterns = [
    path('', home, name='home'),
    path('post/new/', create_post, name='create_post'),
    path('post/<int:pk>/edit/', edit_post, name='edit_post'),
]