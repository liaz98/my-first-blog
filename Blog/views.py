
from django.shortcuts import render, get_object_or_404


def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Blog/post_detail.html', {'post': post})


