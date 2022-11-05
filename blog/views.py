from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Article
from django.contrib.auth.models import User


class ArticleList(ListView):
    model = Article
    template_name = 'blog/article_list.html'

class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/articledetail.html'

class UserList(ListView):
    model = User
    template_name = 'blog/userlist.html'


class UserDetail(DetailView):
    model = User
    template_name = 'blog/userdetail.html'



# Create your views here.

