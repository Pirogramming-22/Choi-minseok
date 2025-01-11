from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=100)       # 제목
    director = models.CharField(max_length=100)    # 감독
    actors = models.CharField(max_length=200)      # 주연
    genre = models.CharField(max_length=50)        # 장르
    rating = models.FloatField()                   # 별점
    running_time = models.IntegerField()           # 러닝타임
    release_year = models.IntegerField()           # 개봉연도
    content = models.TextField()                   # 리뷰 내용

    def __str__(self):
        return self.title
