from ast import Return
from urllib import response
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from . models import Post
from . serializer import PostSerializers
from django.shortcuts import get_object_or_404

from posts import serializer




@api_view(["GET", "POST"])
def homePage(request):

    if request.method == 'POST':
        data = request.data
        response = {
            "message": "hello wolrd",
            "data": data
        }
        return Response(data=response)
    response = {
        "posts": "This is my first post"
    }
    return Response(data=response, status=status.HTTP_200_OK)


# ================== classbased view =======================

class ListPostCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    generics.GenericAPIView

class PostRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    """
    for post retrieving and update and deleting view
    """
    serializer_class = PostSerializers
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    




















# ===============functional based view=======================

# @api_view(["GET", "POST"])
# def listPost(request):
#     # GET METHOD
#     posts = Post.objects.all()

#     # POST METHOD
#     if request.method == "POST":
#         data = request.data
#         serializer = PostSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()

#             response ={
#                 "message": "post created",
#                 "data": serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_204_NO_CONTENT)

#         # GET METHOD
#     serializer = PostSerializers(instance=posts, many=True)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)

    


# @api_view(["GET"])
# def getSinglePost(request, id):
#     post = get_object_or_404(Post, pk=id)

#     serializer = PostSerializers(instance=post)

#     response = {
#         "message": "post",
#         "data": serializer.data
#     }

#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(["PUT"])
# def getUpdatePost(request, id):
#     post = get_object_or_404(Post, pk=id)
#     data = request.data
#     serializer = PostSerializers(instance=post, data=data)

#     if serializer.is_valid():
#         serializer.save()

#         response = {
#             "message": "post update",
#             "data": serializer.data
#         }

#         return Response(data=response, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_204_NO_CONTENT)


# @api_view(["DELETE"])
# def deletePOST(request, id):
#     post = get_object_or_404(Post, pk=id)
   
#     post.delete()

#     response = {
#         "message": "post deleted"
#     }
#     return Response(status=status.HTTP_204_NO_CONTENT)