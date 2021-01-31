from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='blog'),
    path('article/<int:pk>',
         views.ArticleDetailView.as_view(), name='blog_detail'),
    path('add/', views.add_article, name='add_article'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete/<int:article_id>/',
         views.delete_article, name='delete_article'),
]
