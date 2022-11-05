from rest_framework import serializers
from blog.models import Article
from  django.contrib.auth.models import User
class ArticleSerializers(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'