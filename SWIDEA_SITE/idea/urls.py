from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.idea_list, name='idea_list'), #메인페이지(아이디어 관리(List))
  path('icreate/', views.idea_create, name='idea_create'), #아이디어등록
  path('idetail/<int:idea_id>/', views.idea_detail, name='idea_detail'), #아이디어상세페이지
  path('idelete/<int:idea_id>/', views.idea_delete, name='idea_delete'), #아이디어삭제
  path('iupdate/<int:idea_id>/', views.idea_update, name='idea_update'), #아이디어수정
  path('develop', views.develop_list, name='develop_list'), #개발툴 관리(List)
  path('dcreate/', views.develop_create, name='develop_create'), #개발툴등록
  path('ddetail/<int:dvt_id>/', views.develop_detail, name='develop_detail'), #개발툴상세페이지
  path('ddelete/<int:dvt_id>/', views.develop_delete, name='develop_delete'), #
  path('dupdate/<int:dvt_id>/', views.develop_update, name='develop_update'), #개발툴툴수정
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
