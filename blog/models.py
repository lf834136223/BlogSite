from django.db import models
from django.contrib.auth.models import User


"""博客分类"""
class BlogType(models.Model):
	# 一篇博客一种分类
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


"""博客类"""
class Blog(models.Model):
	# 博客标题
    title = models.CharField(max_length=50)
    # 博客所属分类
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    # 博客创建时间,auto_now_add只在第一次创建时添加时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 博客最后更新时间,每一次都回更新时间
    last_update_time = models.DateTimeField(auto_now=True)
    # 博客作者
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	# 博客内容
    content = models.TextField()

    def __str__(self):
        return "博客标题:%s  博客类型：%s" % (self.title, self.blog_type)


class MyInfo(models.Model):
    name = models.CharField(max_length=5)
    gender = models.CharField(max_length=2)

