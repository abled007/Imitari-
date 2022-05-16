from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('post/add', views.PostCreate.as_view(), name="post_create"),
    path('upload/', views.image_upload_view),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>delete', views.PostDelete.as_view(), name="post_delete"),
    # path('accounts/signup/', views.singup_view, name="signup"),
    path('user/<username>/', views.profile, name='profile'),
    path('album/', views.albums_index, name='albums_index'),
]
