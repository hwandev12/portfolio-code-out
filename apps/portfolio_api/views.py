from django.shortcuts import render
from apps.portfolio import models

# rest frameworks
from rest_framework import filters
from .serializers import ContactSerializer
from rest_framework.response import Response
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
        "Taklif Filter": "/contact-taklif/",
        "Shikoyat Filter": "/contact-shikoyat/",
        "Search API": "/contact-search/",
        "Order API": "/contact-order/",
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

# contact TAKLIF filter API
@api_view(["GET"])
def contactTaklifAPI(request):
    contact =  models.Contact.objects.filter(contact_choices="TAKLIF")
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)

# contact SHIKOYAT filter API
@api_view(["GET"])
def contactShikoyatAPI(request):
    contact =  models.Contact.objects.filter(contact_choices="SHIKOYAT")
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
