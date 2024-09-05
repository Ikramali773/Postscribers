from django.urls import path
from .import  views
urlpatterns = [
    path('blog/', views.index, name='index'),
    path('blog/form/', views.form_view),
    path('blog/<int:pk>/', views.blog_details, name='blog-detail'),
    path('blog/edit/<int:pk>/', views.blog_edit, name='blog-edit'),
    path('blog/delete/<int:pk>/', views.post_delete, name='delete'),
    path('blog/myblog/', views.myblog, name='myblog'),
]

