from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, BlogType, MyInfo
from django.http import HttpResponse


def blog_list(request):
    context = {}
    # all()方法得到Blog类的一个集合，是数据库和模型对象交互的接口(api)
    context['blogs'] = Blog.objects.all()
    # context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog_list.html', context)


def blog_detail(request,blog_pk):
    context = {}
    # get_object_or_404 相当于get()，需要有三个参数，这里只有两个，pk是查询条件
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    # context['blogs'] = Blog.objects.all()
    return render_to_response('blog_detail.html', context)


def blogs_with_type(request, blog_type_pk):
    context = {}
    # 严格意义上不能叫blog_type，因为他获取的是一行，包括了主键和type_name。
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response('blogs_with_type.html', context)


def home_page(request):
    return render_to_response('home_page.html')


def connect_me(request):
    context = {}
    context['infos'] = MyInfo.objects.all()
    return render_to_response('show_info.html', context)