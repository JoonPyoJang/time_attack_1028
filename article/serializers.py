from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class ArticleListSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = ("pk", "title", "created_at", "user")


class ArticleAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ("title", "content")