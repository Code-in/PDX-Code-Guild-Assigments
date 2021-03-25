from django.urls import path
from . import views



#app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('create/', views.create_blog, name="create"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('profile/delete/<int:id>/', views.delete_blog, name="delete"),
    path('profile/update/<int:id>/', views.update_blog, name="update"),
    path('posts/', views.posts, name="posts"),
    path('posts/<int:id>/', views.details, name="details")
]
