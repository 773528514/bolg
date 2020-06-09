#coding=UTF-8
from haystack import indexes

from .models import Post

#  PostIndex：实体名字Index 命名规范
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 给title设置索引
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')

    def get_model(self):
        # 返回搜索的模型类
        return Post

    def index_queryset(self, using=None):
        # 返回结果集
        return self.get_model().objects.order_by('-created').all()


