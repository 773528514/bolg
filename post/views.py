# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from haystack.query import SearchQuerySet
from .models import *
from rest_framework import viewsets
from post.serializers import CategorySerializer, TagSerializer, PostSerializer



# Create your views here.

def index_view(request, num='1'):
    page, page_range = Post.get_posts_by_page(num, 2)
    return render(request, 'index.html', context={'page': page, 'page_range': page_range})


def post_details_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        pass
    return render(request, 'details.html', {'post': post})


def category_details_view(request, category_id=None):
    posts = Post.objects.filter(category=category_id).order_by('-created')
    return render(request, 'archive.html', {'posts': posts})


def date_details_view(request, year, month):
    posts = Post.objects.filter(created__year=year, created__month=month).all()
    return render(request, 'archive.html', {'posts': posts})


# 一个字段
# def search_view(request):
#     # 全文搜索的关键字
#     keyword = request.GET.get('q')
#     from django.core.paginator import Paginator
#     search_result = SearchQuerySet().filter(title=keyword).all()
#     paginator = Paginator(search_result,10)
#     page = paginator.page(1)
#     return render(request,'archive.html',{'posts':page.object_list})

def search_view(request):
    from haystack.query import SQ
    from django.core.paginator import Paginator
    # 全文搜索的关键字
    keyword = request.GET.get('q')
    # 搜索结果（返回title、content中包含q的文章对象）
    search_result = SearchQuerySet().filter(SQ(title=keyword) | SQ(content=keyword)).all()
    # 分页
    paginator = Paginator(search_result, 10)
    page = paginator.page(1)
    posts = []

    for result in page.object_list:
        posts.append(result.object)
    return render(request, 'archive.html', {'posts': posts})


class CategoryViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Tag.objects.all().order_by("-date_joined")
    serializer_class = TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

