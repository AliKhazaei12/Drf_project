from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('article_list', Articlelist.as_view(), name='articlelist'),
    path('article_detail/<int:pk>', ArticleDetail.as_view(), name='articledetail'),
    path('user_list', Userlist.as_view(), name='userlist'),
    path('user_detail/<int:pk>', UserDetail.as_view(), name='userdetail')

]
