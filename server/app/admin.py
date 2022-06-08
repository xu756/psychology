from django.contrib import admin
from .models import *

# 配置
admin.site.site_header = '管理后台'
admin.site.site_title = '管理后台'
admin.site.index_title = '管理后台title'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Category, CategoryAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'img', 'category']


admin.site.register(Banner, BannerAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'article_show', 'article_time']


admin.site.register(Article, ArticleAdmin)
