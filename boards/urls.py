from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardListView.as_view(), name='boards'),
    path('<int:pk>/', views.TopicListView.as_view(), name='board_topics'),
    path('<int:pk>/new/', views.new_topic, name='new_topic'),
    path('<int:pk>/topics/<int:topic_pk>/',
         views.PostListView.as_view(), name='topic_posts'),
    path('<int:pk>/topics/<int:topic_pk>/reply/',
         views.reply_topic, name='reply_topic'),
    path('<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',
         views.PostUpdateView.as_view(), name='edit_post'),
    path('delete/<int:board_id>/',
         views.delete_board, name='delete_board'),
    path('delete/topics/<int:topic_id>/',
         views.delete_topic, name='delete_topic'),
    path('delete/posts/<int:post_id>/',
         views.delete_post, name='delete_post'),
]
