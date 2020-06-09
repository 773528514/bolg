# coding=UTF-8

# 全局上下文
# 把页面的'分类'‘归档’'近期文章'  存储在全局上下文
from .models import *
from datetime import date
from django.db.models import *


def slider_context_processor(request):
    context = {}
    # 获取'分类'（category）信息
    context['category'] = Post.objects.values('category', 'category__name').annotate(count=Count('*'))
    # ‘归档’
    archive = Post.objects.values('created').order_by('-created')
    context['archive'] = archive
    # '近期文章'
    context['recent'] = Post.objects.order_by('-created').all()[:5]
    return context

# def get_archive():
#     s = set()
#     for t in Post.objects.values('created'):
#         s.add(str(t['created'].year) + "-" + str(t['created'].month))
#     archive = []
#     for time in s:
#         year = time.split('-')[0]
#         month = time.split('-')[1]
#         item = {'created': date(year=int(year), month=int(month), day=1),
#                 'count': Post.objects.filter(created__year=year, created__month=month).count()}
#         archive.append(item)
#     return archive
