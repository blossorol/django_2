from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)


def __str__(self):
    return self.name


class Meta:
    verbose_name = "用户"
    verbose_name_plural = "用户"


class Article(models.Model):
    """文章详细内容"""
    article_title = models.CharField(verbose_name='文章标题', max_length=100)
    article_content = models.TextField(verbose_name='正文', default='')
    article_create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    article_modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    article_read_nums = models.IntegerField(verbose_name='阅读量', default=0)
    article_like_nums = models.IntegerField(verbose_name='点赞量', default=0)

    class Meta:
        verbose_name = '文章详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article_content


class Account(models.Model):
    password=models.CharField(max_length=200)
    name=models.CharField(max_length=20)