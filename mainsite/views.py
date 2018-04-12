from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType

def blog_list(request):
    context = {}
    context['blog_list'] = Blog.objects.all()
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('mainsite/blog_list.html', context)

def blog_detail(request, blog_pk):
    context = {}
    context['blog_detail'] = get_object_or_404(Blog,pk=blog_pk)
    return render_to_response('mainsite/blog_detail.html', context)

def blog_type_selected(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context['blog_all_list'] = Blog.objects.all()
    context['blog_detail_selected'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()

    #统计个标签的文章数量

    blog_all_type = list(BlogType.objects.all())

    blog_types_count = []

    for i in range(0,blog_all_type.__len__()):
        blog_type_count = Blog.objects.all().filter(blog_type=blog_all_type[i]).count()
        blog_types_count.append(blog_type_count)

    context['blog_types_count'] = blog_types_count
    
    return render_to_response('mainsite/blog_type_selected.html', context)



