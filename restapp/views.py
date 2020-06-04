from django.shortcuts import render
from restapp.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def MovieList(request):
    if request.method == 'GET':
        obj = Movie.objects.all()
        serializer = MovieSerializer(obj,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def MovieDetail(request,pk):
    try:
        obj = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer= MovieSerializer(obj,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_200_OK)
