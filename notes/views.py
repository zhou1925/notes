from django.shortcuts import render

from rest_framework import generics

from .models import Note
from .api.serializers import NoteSerializer


class NoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer