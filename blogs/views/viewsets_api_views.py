from typing_extensions import dataclass_transform
from rest_framework import viewsets,status
from uritemplate import partial
from blogs.models import BlogModel
from blogs.serializers import BlogSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class BlogViewSets(viewsets.ViewSet):
    def list(self,request):
        queryset = BlogModel.objects.all()
        serializer = BlogSerializer(queryset,many = True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk = None):
        queryset =BlogModel.objects.all()
        if pk is not None:
            blog = get_object_or_404(queryset,pk=pk)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        
    def create_data(self,request):
        data_to_create = request.data
        serializer_data =BlogSerializer(data= data_to_create)
        if serializer_data.is_valid():
            serializer_data.save()
      
            return Response(serializer_data.data)
        
    def update(self, request, pk=None):
        data_to_update = BlogModel.objects.get(pk = pk)
        serializer = BlogSerializer(
            data_to_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def destroy(self,request,pk=None):
        data_to_delete = BlogModel.objects.get(pk = pk)
        data_to_delete.delete()
        return Response("data deleted successfully")       

class BlogModelViewSets(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer