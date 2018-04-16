from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class BlogType(models.Model):
    type_name = models.CharField(max_length=15,verbose_name="博文类型")

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题")
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_updated_time = models.DateTimeField(auto_now=True, verbose_name="最后修改的时间")
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name="博文类型")

    def read_num(self):
        return self.readnum.read_num
        
    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-create_time',]

class ReadNum(models.Model):
    read_num = models.IntegerField(default=0, verbose_name="阅读计数")
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING, verbose_name="博客外键")
