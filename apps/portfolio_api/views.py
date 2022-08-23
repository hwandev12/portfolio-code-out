from django.shortcuts import render
from apps.portfolio import models

# rest frameworks
from rest_framework import viewsets
from .serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics


# API userset
@api_view(["GET"])
def contact_api(request):
    api_urls = {
        "List": "/contact-list/",
        "Detail View": "/contact-detail/<str:pk>/",
        "Create": "/contact-create/",
        "Update": "/contact-update/<str:pk>/",
        "Delete": "/contact-delete/<str:pk>",
    }

    return Response(api_urls)


@api_view(["GET"])
def contactList(request):
    contact = models.Contact.objects.all()
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def contactDetail(request, pk):
    contact = models.Contact.objects.get(id=pk)
    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def contactCreate(request):
	serializer = ContactSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(["POST"])
def contactUpdate(request, pk):
	contact = models.Contact.objects.get(id=pk)
	serializer = ContactSerializer(instance=contact, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(["DELETE"])
def contactDelete(request, pk):
	contact = models.Contact.objects.get(id=pk)
	contact.delete()

	return Response("API successfully deleted!")