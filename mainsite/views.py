from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType

def blog_list(request):
    context = {}
    context['blog_list'] = Blog.objects.all()
    return render_to_response('mainsite/blog_list.html', context)

def blog_detail(request, blog_pk):
    context = {}
    context['blog_detail'] = get_object_or_404(Blog,pk=blog_pk)
    return render_to_response('mainsite/blog_detail.html', context)

def blog_type_selected(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context['blog_detail_selected'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response('mainsite/blog_type_selected.html', context)



