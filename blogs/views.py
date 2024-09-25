from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from blogs.forms import BlogPostForm, BlogEditForm
from blogs.models import BlogPost


def home(request):
    posts = BlogPost.objects.all().order_by('-date_added')
    context = {'posts': posts, 'request': request}
    return render(request, 'blogs/home.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.owner = request.user
            blog_post.save()
            return redirect('blogs:home')
    else:
        form = BlogPostForm()
    return render(request, 'blogs/post.html', {'form': form})

@login_required
def edit_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = BlogEditForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    else:
        form = BlogEditForm(instance=blog_post)
    return render(request, 'blogs/edit.html', {'form': form})