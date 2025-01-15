from django.shortcuts import render, redirect
from .models import Idea, Devtool
from .forms import IdeaForm, DevtoolForm

# Create your views here.
def idea_list(request):
  ideas = Idea.objects.all()
  context={"ideas":ideas}
  return render(request, 'idea/idea_list.html', context)

def idea_create(request):
  if request.method == 'POST': #폼 제출 시
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
      form.save() #유효하면 db에저장
      return redirect('idea_detail', form.instance.id)
  else: #페이지 처음 열 때
    form = IdeaForm()
  return render(request, 'idea/idea_create.html', {'form':form})

def develop_create(request):
  if request.method == 'POST': #폼 제출 시
    form = DevtoolForm(request.POST, request.FILES)
    if form.is_valid():
      form.save() #유효하면 db에저장
      return redirect('develop_detail', form.instance.id)
  else: #페이지 처음 열 때
    form = DevtoolForm()
  return render(request, 'idea/develop_create.html', {'form':form})

def idea_update(request, idea_id):
  idea = Idea.objects.get(id=idea_id)
  if request.method == 'POST': #폼 제출 시
    form = IdeaForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
      form.save()
      return redirect('idea_detail', idea_id)
  else: #페이지 처음 열 때
    form = IdeaForm(instance=idea)
  return render(request, 'idea/idea_update.html', {'form':form})

def develop_update(request, dvt_id):
  dvt = Devtool.objects.get(id=dvt_id)
  if request.method == 'POST': #폼 제출 시
    form = DevtoolForm(request.POST, request.FILES, instance=dvt)
    if form.is_valid():
      form.save()
      return redirect('develop_detail', dvt_id)
  else: #페이지 처음 열 때
    form = DevtoolForm(instance=dvt)
  return render(request, 'idea/develop_update.html', {'form':form})

def idea_delete(request, idea_id):
  idea = Idea.objects.get(id=idea_id)
  idea.delete()
  return redirect('idea_list')

def develop_delete(request, dvt_id):
  dvt = Devtool.objects.get(id=dvt_id)
  dvt.delete()
  return redirect('develop_list')

def idea_detail(request, idea_id):
  idea = Idea.objects.get(id=idea_id)
  context = {"idea":idea}
  return render(request, 'idea/idea_detail.html', context=context)

def develop_list(request):
  devtools = Devtool.objects.all()
  context = {"dtls":devtools}
  return render(request, 'idea/develop_list.html', context=context)

def develop_detail(request, dvt_id):
  dvt = Devtool.objects.get(id=dvt_id)
  context = {"dvt":dvt}
  return render(request, 'idea/develop_detail.html', context=context)