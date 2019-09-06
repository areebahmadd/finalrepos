from django.urls import path

from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView,
)

from . import views

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    #path('', BlogListView.as_view(), name='home'),
    path('',views.PostList.as_view()),
    path('<int:pk>/',views.PostDetail.as_view()),
    path('posts/create/',views.PostCreate.as_view()),
    path('posts/<int:pk>/',views.PostDetail.as_view()),

]
