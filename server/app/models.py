from django.db import models
from app.storage import ImageStorage

from ckeditor.fields import RichTextField


# 分类
class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=100, unique=True, verbose_name='分类名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


# 轮播图
class Banner(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='轮播图名称')
    img = models.ImageField(upload_to='banner', storage=ImageStorage(), verbose_name='轮播图')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='name', verbose_name='分类')
    bananer_show = models.BooleanField(default=True, verbose_name='是否显示')
    banner_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


# 文章
class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=100, verbose_name='文章标题')
    note = models.CharField(max_length=100, verbose_name='文章简介')
    content = RichTextField(verbose_name='文章内容')
    img = models.ImageField(upload_to='article', storage=ImageStorage(), verbose_name='文章图片')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='name', verbose_name='分类')
    article_show = models.BooleanField(default=True, verbose_name='是否显示')
    article_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
