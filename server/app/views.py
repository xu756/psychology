from django.http import JsonResponse
from app.models import *


# Create your views here.
def getdefault(request):
    res = {}
    id = request.GET.get('id')
    category = Category.objects.filter(id=id).values('name').first()['name']
    res['banner'] = list(Banner.objects.filter(category=category, bananer_show=True).values('id', 'img'))[0:3]
    res['article'] = list(
        Article.objects.filter(category=category, article_show=True).values('id', 'title', 'img', 'article_time',
                                                                            'note'))[0:5]
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})
