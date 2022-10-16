from ast import Return
from urllib import response
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
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

class ListPostCreateView(APIView):

    """
    for creating and listing the post
    """
    serializer_class = PostSerializers

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        serializer = self.serializer_class(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "post created",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostRetrieveUpdateDeleteView(APIView):
    """
    for post retrieving and update and deleting view
    """
    serializer_class = PostSerializers

    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)

        serializer = self.serializer_class(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        post = get_object_or_404(Post, pk=id)

        data = request.data
        serializer = self.serializer_class(instance=post, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "post updated",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




















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