from django.shortcuts import render, redirect
from .models import Post, Comment, CustomUser, Like
# Create your views here.
def index(request):
  posts = Post.objects.all()
  context = {
    'posts': posts
  }
  return render(request, 'pirostagram/index.html', context)

def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  comments = Comment.objects.filter(post=post)
  context = {
    'post': post,
    'comments': comments,
  }
  return render(request, 'pirostagram/post_detail.html', context)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['post_id']
    user_id = req['user'] #user.id
    post = Post.objects.get(id=post_id)
    user = CustomUser.objects.get(id=user_id)
    like, created = Like.objects.get_or_create(post=post, user=user)

    if created:
        post.likes_count += 1
    else:
       post.likes_count -=1
       like.delete()
    post.save()

    return JsonResponse({
       'post_id': post_id, 
       'likes_count': post.likes_count
       }) 

@csrf_exempt
def comment_ajax(request):
  req = json.loads(request.body)
  post_id= req['post_id']
  user_id= req['user']
  content= req['content']
  post = Post.objects.get(id=post_id)
  user = CustomUser.objects.get(id=user_id)
  if post_id and user_id and content:
    new_comment = Comment.objects.create(post=post, user=user, content=content)
    new_comment.save()
    return JsonResponse({
       'id': new_comment.id,
      'user': new_comment.user.username,
      'content': new_comment.content,
      'comment_id' : new_comment.id
    })
  
  return JsonResponse({'message': 'error'})

@csrf_exempt
def del_ajax(request):
  req = json.loads(request.body)
  comment_id = req['comment_id']
  comment = Comment.objects.get(id=comment_id)
  comment.delete()
  return JsonResponse({'comment_id': comment_id})