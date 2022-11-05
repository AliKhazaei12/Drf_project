from django.urls import path
from .views import *

app_name='article'


urlpatterns=[
    path('article_list',ArticleList.as_view(),name='articlelist'),
    path('detail/<int:pk>/',ArticleDetail.as_view(),name='articledetail'),
    path('list',UserList.as_view(),name='user_list'),
    path('detail/<int:pk>',UserDetail.as_view(),name='user_detail')
]