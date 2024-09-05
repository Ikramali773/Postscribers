from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentModelForm
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):    
        blogs=PostModel.objects.all()
        return render(request, 'blog/index.html', {'blogs':blogs})

@login_required
def form_view(request):
    if request.method=='POST':
        form=PostModelForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.date_created=datetime.now()
            instance.save()
            return redirect('index')
    else:
        form=PostModelForm()
    return render(request, 'blog/forms.html', { 'form':form})

@login_required
def blog_details(request,pk):
     post=PostModel.objects.get(id=pk)
     if request.method=='POST':
          c_form=CommentModelForm(request.POST)
          if c_form.is_valid():
               instance=c_form.save(commit=False)
               instance.user=request.user
               instance.post=post
               instance.save()
               return redirect('blog-detail', post.id)

     else:
          c_form=CommentModelForm()
     context={
          'post':post,
          'c_form':c_form
     }
     
     return render(request, 'blog/blog_details.html', context)

@login_required
def blog_edit(request,pk):
     post=PostModel.objects.get(id=pk)
     if request.method=='POST':
          form=PostUpdateForm(request.POST, instance=post)
          if form.is_valid():
            form.save()
            return redirect('blog-detail', pk=post.id)
     else:
          form=PostUpdateForm(instance=post)
     context={
          'post':post,
          'form':form
     }
     
     return render(request, 'blog/blog_edit.html', context)

@login_required
def post_delete(request, pk):
    post=PostModel.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, 'blog/blog_delete.html', {'post':post})

@login_required
def myblog(request):
     current_user=request.user
     post=PostModel.objects.raw(f"Select * from public.blogapp_postmodel where author_id = {current_user.id} Order by date_created ASC; ")
     return render(request, 'blog/myblog.html', {'post':post})

