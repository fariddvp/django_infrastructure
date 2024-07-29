from rest_framework import serializers
from content.models import Post, Tag, PostMedia
from location.serializers import LocationSerializer
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Serializers : Using Model Serializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')

    # Return name of attr anc check validations for one attr
    def validate_title(self, attr):
        return attr

    # Check validation for multiple attrs
    def validate(self, attrs):
        if len(attrs['title']) > 10:
            raise ValidationError(_("Title can not more than 10 characters."))
        return super().validate(attrs)
    

# Serialize for return a attr with a method
class TagDetailSeralizer(serializers.ModelSerializer):
    # For run method
    posts = serializers.SerializerMethodField()
    
    class Meta:
        model = Tag
        fields = ('id', 'title', 'posts')

    def get_posts(self, obj):
        return obj.posts.count()
    

class PostMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostMedia
        fields = ('id', 'media_type', 'media_file')



class PostDetailSerializer(serializers.ModelSerializer):
    
    # user = serializers.CharField(source='user.username')

    # Nested Serializer
    location = LocationSerializer()
    
    # Nested Serializer
    media = PostMediaSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'caption', 'location', 'media')
