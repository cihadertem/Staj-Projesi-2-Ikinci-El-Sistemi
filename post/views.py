from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post,Category
from .forms import PostForm
from django.core.paginator import Paginator
from django.shortcuts import render



def post_index(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
            post_list = post_list.filter(title__icontains=query)
    paginator = Paginator(post_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'home.html', {'posts': posts})


def post_detail(request,id):
    post= get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.yazar = request.user
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }

    return render(request, "form2.html", context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.yazar = request.user
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, "form2.html", context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("home")

def category_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'post/category.html', context)
def category_index_view(request, category_id):
    post_list = Post.objects.filter(Q(category=category_id) | Q(category__parent=category_id))
    query = request.GET.get('q')
    if query:
            post_list = post_list.filter(title__icontains=query)
    paginator = Paginator(post_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'home.html', {'posts': posts})

def user_post_index(request):
    post_list = Post.objects.filter(yazar=request.user)
    query = request.GET.get('q')
    if query:
            post_list = post_list.filter(title__icontains=query)
    paginator = Paginator(post_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'home.html', {'posts': posts})
# Create your views here.
