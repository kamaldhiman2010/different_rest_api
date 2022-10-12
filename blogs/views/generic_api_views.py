from rest_framework import generics
from blogs.models import BlogModel
from blogs.serializers import BlogSerializer

class BlogListView(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class =BlogSerializer 
    
class BlogCreateView(generics.CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    
class BlogListCreateAPI(generics.ListCreateAPIView):
    queryset =BlogModel.objects.all()
    serializer_class =BlogSerializer
    
class BlogRetriveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset =BlogModel.objects.all()
    serializer_class =BlogSerializer