from django.shortcuts import render
from rest_framework import viewsets

from .serializers import StorySerializer
from .models import Story

# Create your views here.
class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('name')
    serializer_class = StorySerializer