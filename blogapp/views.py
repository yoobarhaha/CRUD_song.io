from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})
@csrf_exempt
def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})
@csrf_exempt
def new(request):
    return render(request, 'new.html')
@csrf_exempt
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
@csrf_exempt
def delete(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    blog_detail.delete()
    return redirect('home')
@csrf_exempt
def edit(request,blog_id):
    if(request.method == 'POST'):
        blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html', {'blog':blog_detail})
@csrf_exempt
def update(request, blog_id):
    blog= get_object_or_404(Blog, pk= blog_id)
    if(request.method == 'POST'):
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
    return redirect('/blog/'+str(blog.id))