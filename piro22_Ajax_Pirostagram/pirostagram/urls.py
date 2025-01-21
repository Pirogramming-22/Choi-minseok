from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('comment_ajax/', views.comment_ajax, name='comment_ajax'),
    path('del_ajax/', views.del_ajax, name='del_ajax'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
if settings.DEBUG:  # 개발 환경에서만 미디어 파일 서빙
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)