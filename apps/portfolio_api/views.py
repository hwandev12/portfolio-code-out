from django.shortcuts import render
from apps.portfolio import models

# rest frameworks
from rest_framework import filters
from .serializers import ContactSerializer, PostSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django.contrib.auth import get_user_model

User = get_user_model()


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


# API userset
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def contact_api(request):
    api_urls = {
        "List": "/contact-list/",
        "Detail View": "/contact-detail/<str:pk>/",
        "Create": "/contact-create/",
        "Update": "/contact-update/<str:pk>/",
        "Delete": "/contact-delete/<str:pk>",
        "Taklif Filter": "/contact-taklif/",
        "Shikoyat Filter": "/contact-shikoyat/",
        "Search API": "/contact-search/",
        "Order API": "/contact-order/",
    }

    return Response(api_urls)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def contactList(request):
    contact = models.Contact.objects.all()
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def contactDetail(request, pk):
    contact = models.Contact.objects.get(id=pk)
    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def contactCreate(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def contactUpdate(request, pk):
    contact = models.Contact.objects.get(id=pk)
    serializer = ContactSerializer(instance=contact, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes((permissions.AllowAny,))
def contactDelete(request, pk):
    contact = models.Contact.objects.get(id=pk)
    contact.delete()

    return Response("API successfully deleted!")


# contact TAKLIF filter API
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def contactTaklifAPI(request):
    contact = models.Contact.objects.filter(contact_choices="TAKLIF")
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)


# contact SHIKOYAT filter API
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def contactShikoyatAPI(request):
    contact = models.Contact.objects.filter(contact_choices="SHIKOYAT")
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)


# Search contacts
class ContactSearchAPI(generics.ListAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['your_name', 'email', 'contact_choices']


contactSearch = ContactSearchAPI.as_view()


class ContactOrderAPI(generics.ListAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.OrderingFilter]
    search_fields = '__all__'


contactOrder = ContactOrderAPI.as_view()


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def postAPI_lists(request):
    post = models.Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def postDetail(request, pk):
    post = models.Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def postCreate(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def postUpdate(request, pk):
    post = models.Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes((permissions.AllowAny,))
def postDelete(request, pk):
    post = models.Post.objects.get(id=pk)
    post.delete()

    return Response("Item successfully deleted!")


@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UserLists(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)
