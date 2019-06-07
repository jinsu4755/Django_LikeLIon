"""
추후 파일이 많아지면 메인 url을 관리하기 힘듦, 따라서 앱별로
urls를 나누어 관리하고 import 시킨다.
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'crud'
urlpatterns = [
    path('', views.main, name="main"),
    path("post/", views.post, name="post"),
    path("detail/<int:article_id>/", views.detail, name="detail"),
    path("edit/<int:article_id>/", views.edit, name="edit"),
    path("delete/<int:article_id>/", views.delete, name="delete"),
    path("comment_del/<int:comment_id>/", views.comment_del, name="comment_del"),
    path("comment_edit/<int:comment_id>/", views.comment_edit, name="comment_edit"),
    path("hashtag/", views.hashtagform, name="hashtag"),
    path("<int:hashtag_id>/search/", views.search, name="search"),
    # views 파일의 main 함수를 보여준다 main 이라는 이름으로
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
