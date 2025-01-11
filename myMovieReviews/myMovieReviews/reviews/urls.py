from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),            # 리뷰 리스트
    path('review/<int:pk>/', views.review_detail, name='review_detail'),  # 리뷰 디테일
    path('review/new/', views.review_create, name='review_create'),       # 리뷰 작성
    path('review/<int:pk>/edit/', views.review_update, name='review_update'),  # 리뷰 수정
    path('review/<int:pk>/delete/', views.review_delete, name='review_delete'),  # 리뷰 삭제
]
