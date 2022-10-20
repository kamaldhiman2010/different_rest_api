from django.shortcuts import get_object_or_404
from rest_framework import generics,status
from blogs.models import BlogModel
from blogs.serializers import BlogSerializer
from rest_framework.response import Response

from rest_framework.views import APIView
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
    

class CustomMixin:
    serializer_class = None
    model_class = None

    def get(self, request, blog_id):
        obj = get_object_or_404(
            self.model_class, id=blog_id
        )
        title = obj.title
        print(title)
        data = {"title": title, "id": blog_id}
        serializer = self.serializer_class(
            data=data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request, blog_id):

        obj = get_object_or_404(
            self.model_class, id=blog_id
        )
        obj.delete()
        return Response(
            "deleted", status.HTTP_204_NO_CONTENT
        )


class FavoriteViewSet(CustomMixin, APIView):
    serializer_class = BlogSerializer
    model_class = BlogModel
