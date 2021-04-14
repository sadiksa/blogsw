from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('post/<int:pk>/', views.PostView.as_view(), name="postdetail"),
    path('add_post/', views.AddPostView.as_view(), name="addpost"),
    path('add_category/', views.AddCategoryView.as_view(), name="addcategory"),
    path('post/<int:pk>/edit/', views.EditPostView.as_view(), name="editpost"),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name="deletepost"),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('categories/', views.CategoryListView, name='categories'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('search/', views.SearchView, name='search'),
]
# as_view() for class based views
# pk primary key is unique for each model object (instance)
