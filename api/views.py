from .Serializer import ArticleSerializers,UserSerializers
from blog.models import Article
from .permission import *
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from  django.contrib.auth.models import User
class Articlelist(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

class ArticleDetail(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = (IsStaffOrReadOnly,IsAuthorOrReadOnly)

class Userlist(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUserOrStaffReadOnly,)



# Create your views here.
