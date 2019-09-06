from rest_framework import serializers
from blog.models import Post

# class PostSerializer(serializers.ModelSerializer):
#     #id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     author = serializers.CharField(required=True,allow_blank=False)


#         def create(self, validated_data):

#             return Post.objects.create(**validated_data)

#         def update(self, instance, validated_data):

#             instance.title = validated_data.get('title', instance.title)
#             instance.author = validated_data.get('author',instance.author)
#             return instance


from . import models

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','title','author','body')
        model = models.Post