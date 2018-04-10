from django.db import models
from django.contrib.auth.models import User

class BlogType(models.Model):
    type_name = models.CharField(max_length=15,verbose_name="博文类型")

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_updated_time = models.DateTimeField(auto_now=True, verbose_name="最后修改的时间")
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name="博文类型")

    def __str__(self):
        return "<Blog: %s>" % self.title
