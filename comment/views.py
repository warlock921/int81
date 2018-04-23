from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .models import Comment

#更新评论的view方法
def update_comment(request):
    user = request.user
    comment_content = request.POST.get('comment_content','')

    object_id = int(request.POST.get('object_id',''))
    content_type = request.POST.get('content_type','')
    #评论通用模型，不仅可以评论博客，还可以评论其他模块
    model_class = ContentType.objects.get(model=content_type).model_class()
    model_obj = model_class.objects.get(pk=object_id)

    if comment_content == '':
        return render(request, 'error.html', {'message':"评论内容不能为空！！"})
    else:
        #评论写数据库
        comment = Comment()
        comment.comment_user = user
        comment.comment_content = comment_content
        comment.content_object = model_obj
        comment.save()

        #获取当前页面信息，如果获取不到，就跳转主页
        referer = request.META.get('HTTP_REFERER', reverse('home'))
        return redirect(referer)




