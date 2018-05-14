from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, verbose_name="评论的对象")
    object_id = models.PositiveIntegerField(verbose_name="对象ID")
    content_object = GenericForeignKey('content_type', 'object_id')

    comment_content = models.TextField(verbose_name="评论内容")
    comment_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="评论用户")
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")

    def __str__(self):
        return self.comment_user

    class Meta:
        ordering = ['-comment_time']