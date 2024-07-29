from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from content.models import Tag, Post, PostMedia
from content.serializers import TagDetailSeralizer, TagSerializer, PostDetailSerializer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.

# API with Generic View for => create(post) and show list(get) of tags in db
class TagListCreateAPI(ListCreateAPIView):

    # Any user for access to API should send request with access token
    permission_classes = (IsAuthenticated,)

    # Custom permission class for login users ans get access to them
    permission_classes = (SessionAuthentication, JWTAuthentication)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)


# API with Generic View for => show list(get) tags in db
class TagListAPI(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)

# API with 2 methods:

# 1.API with Generic View for => create(post) tags in db
class TagCreateAPI(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)


# 2.API with API View for get and post
class TagAnyAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        tags = Tag.objects.filter(pk=pk)
        tag = get_object_or_404(Tag, **{'pk':pk})
        serializer = TagDetailSeralizer(tag)
        if not tags.exists():
            return Response('Not Found.', status=status.HTTP_404_NOT_FOUND)
        tag = tags.first()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwwargs):
        serializer = TagDetailSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

# API for Post model with APIView  
class PostDetailAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    
# API for Post Media model with APIView
class PostMediaAPI(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
