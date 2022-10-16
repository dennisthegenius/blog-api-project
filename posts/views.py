from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from . models import Post
from .serializer import PostSerializers
from posts import serializer


class  PostViewSet(viewsets.ViewSet):
    def list(self, request:Request):
        queryset = Post.objects.all()
        serializer = PostSerializers(instance=queryset, many=True)

        response = {
            "message":"all posts",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

    def retrieve(self, request:Request, pk=None):
        post = get_object_or_404(Post,pk=pk)
        serializer = PostSerializers(instance=post)
        response = {
            "message":"post",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
