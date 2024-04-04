from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Paragraph
from .serializers import ParagraphSerializer

class ParagraphListCreateAPIView(generics.ListCreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

class ParagraphDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

