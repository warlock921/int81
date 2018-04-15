from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

#统计各年月所含的文章数量方法
# def blog_date_count():
#     all_blogs = list(Blog.objects.filter(create_time__year=year, create_time__month=month))
#     all_blogs_date =list(all_blogs.values_list())
#     blog_date_dict = {}

#     for date in range(0,)

#分页方法，需要传入request、每页需要的文章数、用于分页的文章总集合
def page_2_page(request, num_of_page, need_blogs):
    # all_blogs = Blog.objects.all()
    #分页处理
    paginator = Paginator(need_blogs, num_of_page) #分页处理，num_of_page代表每页的文章数
    #获取页面传来参数（第N页）
    page = request.GET.get('page')
    page_num = paginator.get_page(page)
    return page_num #返回一个分页后的数据集

#页码缩减方法
def page_2_range(page_num):
    #获取当前页码
    current_page = page_num.number
    #获取当前页码的前两页
    behind_page = list(range(max(current_page-2,1),current_page))
    #获取当前页码的后两页
    after_page = list(range(current_page,min(page_num.paginator.num_pages,current_page+2)+1))
    #组合页码列表
    page_range = behind_page + after_page

    #判断第一页或最后一页的页码，如果页码之间间隔超过2页，添加"..."
    if page_range[0] - 1 >= 2 :
        page_range.insert(0,"...")
    if page_num.paginator.num_pages - page_range[-1] >= 2 :
        page_range.append("...")
        

    #判断页码，添加第一页和最后一页
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != page_num.paginator.num_pages:
        page_range.append(page_num.paginator.num_pages)

    return page_range

def blog_list(request):
    all_blogs = Blog.objects.all()
    page_num = page_2_page(request, 4, all_blogs) #调用分页方法，4 - 代表每页的文章数
    page_range = page_2_range(page_num) #调用页码缩减方法，传入的是分页后的数据
    context = {}
    context['blog_list'] = all_blogs
    context['blog_types'] = BlogType.objects.all()
    context['blog_types_dict'] = blog_article_count()
    #传递分页后的blog文章集合信息
    context['page_num'] = page_num
    #缩减后的页码范围
    context['page_range'] = page_range
    context['blogs_date'] = Blog.objects.dates('create_time','month',order="DESC")
    return render_to_response('mainsite/blog_list.html', context)

def blog_detail(request, blog_pk):
    context = {}
    current_blog = get_object_or_404(Blog,pk=blog_pk)
    context['blog_detail'] = current_blog

    #查询前一条博客和后一条博客
    previous_blog = Blog.objects.filter(create_time__gt=current_blog.create_time).last()
    next_blog = Blog.objects.filter(create_time__lt=current_blog.create_time).first()
    context['previous_blog'] = previous_blog
    context['next_blog'] = next_blog

    context['blog_types_dict'] = blog_article_count()
    return render_to_response('mainsite/blog_detail.html', context)

def blog_type_selected(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    blog_detail_selected = Blog.objects.filter(blog_type=blog_type)
    #分页
    page_num = page_2_page(request, 4, blog_detail_selected) #调用分页方法，4 - 代表每页的文章数
    page_range = page_2_range(page_num) #调用页码缩减方法，传入的是分页后的数据

    context['blog_all_list'] = Blog.objects.all()
    # context['blog_detail_selected'] = blog_detail_selected
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    context['blog_types_dict'] = blog_article_count() #调用博客文章计数方法
    #传递分页后的blog文章集合信息
    context['page_num'] = page_num
    #缩减后的页码范围
    context['page_range'] = page_range
    
    return render_to_response('mainsite/blog_type_selected.html', context)

def blog_date_selected(request, year, month):
    context = {}
    blog_dates = Blog.objects.filter(create_time__year=year, create_time__month=month)
    print(blog_dates)
    #分页
    page_num = page_2_page(request, 4, blog_dates) #调用分页方法，4 - 代表每页的文章数
    page_range = page_2_range(page_num) #调用页码缩减方法，传入的是分页后的数据

    context['blog_dates'] = blog_dates
    context['blog_all_list'] = Blog.objects.all()

    context['blog_types_dict'] = blog_article_count() #调用博客文章计数方法
    #传递分页后的blog文章集合信息
    context['page_num'] = page_num
    #缩减后的页码范围
    context['page_range'] = page_range
    return render_to_response('mainsite/blog_date_selected.html', context)