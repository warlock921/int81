from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType

#统计各文章类型所含的文章数量方法
def blog_article_count():
    
    # list(BlogType.objects.values_list('type_name',flat=True))  这是将BlogType中的类型结果集转换为列表，只取一个指定的值的方法
    #取BlogType的所有类型，并转化为一个列表
    blog_all_type = list(BlogType.objects.all())
    #取BlogType的所有类型的id和值，组成列表
    blog_types_kind = list(BlogType.objects.values_list())
    #定义一个字典
    blog_types_dict = {}
    #用for循环组装字典
    for i in range(0,blog_all_type.__len__()):
        #计算某一个博客类型中有多少篇文章，这里是一个int值
        blog_type_count = Blog.objects.all().filter(blog_type=blog_all_type[i]).count()
        #组装字典，该字典是以id和博客类型组成的元组作为键，博客类型的名称作为值
        blog_types_dict[blog_types_kind[i]] = blog_type_count
    return blog_types_dict

def blog_list(request):
    context = {}
    context['blog_list'] = Blog.objects.all()
    context['blog_types'] = BlogType.objects.all()
    context['blog_types_dict'] = blog_article_count()
    return render_to_response('mainsite/blog_list.html', context)

def blog_detail(request, blog_pk):
    context = {}
    context['blog_detail'] = get_object_or_404(Blog,pk=blog_pk)
    context['blog_types_dict'] = blog_article_count()
    return render_to_response('mainsite/blog_detail.html', context)

def blog_type_selected(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context['blog_all_list'] = Blog.objects.all()
    context['blog_detail_selected'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()

    # #统计各文章类型所含的文章数量
    # # list(BlogType.objects.values_list('type_name',flat=True))  这是将BlogType中的类型结果集转换为列表，只取一个指定的值的方法
    # #取BlogType的所有类型，并转化为一个列表
    # blog_all_type = list(BlogType.objects.all())
    # #取BlogType的所有类型的id和值，组成列表
    # blog_types_kind = list(BlogType.objects.values_list())
    # #定义一个字典
    # blog_types_dict = {}
    # #用for循环组装字典
    # for i in range(0,blog_all_type.__len__()):
    #     #计算某一个博客类型中有多少篇文章，这里是一个int值
    #     blog_type_count = Blog.objects.all().filter(blog_type=blog_all_type[i]).count()
    #     #组装字典，该字典是以id和博客类型组成的元组作为键，博客类型的名称作为值
    #     blog_types_dict[blog_types_kind[i]] = blog_type_count
    # #传送组装好的字典到前端
    context['blog_types_dict'] = blog_article_count()
    
    return render_to_response('mainsite/blog_type_selected.html', context)



