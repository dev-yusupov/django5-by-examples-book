from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView

from .models import Post

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"

# Create your views here.
# def post_list(request):
#     post_list = Post.published.all()
    
#     paginator = Paginator(post_list, 3)
#     page_number = request.GET.get('page', 1)

#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         posts = paginator.page(1)

#     return render(
#         request,
#         'blog/post/list.html',
#         {
#             "posts": posts
#         }
#     )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    
    return render(
        request,
        'blog/post/detail.html',
        {
            "post": post
        }
    )