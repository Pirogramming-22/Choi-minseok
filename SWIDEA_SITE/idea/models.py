from django.db import models

class Devtool(models.Model):
  name=models.CharField(max_length=50)
  kind=models.CharField(max_length=50)
  content=models.TextField()

  def __str__(self):
    return self.name

# Create your models here.
class Idea(models.Model):
  title=models.CharField(max_length=50)
  image=models.ImageField()
  content=models.TextField()
  interest=models.IntegerField()
  devtool=models.ForeignKey(Devtool, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


