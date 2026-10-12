from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status

class BookView(APIView):
    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data) 
    
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateView(APIView):
    def put(self,request,pk):
        books=Book.objects.get(pk=pk)
        serializer=BookSerializer(books,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        books=Book.objects.get(pk=pk)
        serializer=BookSerializer(books,data=request.data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self,request,pk):
        book=Book.objects.get(pk=pk)
        book.delete()
        return Response({"message":"deleted successfully"},status=status.HTTP_200_OK)