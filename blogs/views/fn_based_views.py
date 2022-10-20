from select import select
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from uritemplate import partial
from blogs.serializers import  BlogSerializer
from blogs.models import BlogModel,Movie,Director

@api_view(['GET','POST'])
def blog_view(request):
    if request.method == 'GET':
        blogs = BlogModel.objects.all()
        serializer = BlogSerializer(blogs,many =True)
        return Response({
            'success' :True,
            'message' : 'Get request fulfilled !!',
            'data' : serializer.data
        })
    if request.method == 'POST':
        serializers = BlogSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({
                'success' :True,
                'message' : 'Post request fulfilled !!',
                'data' : serializers.data
            })
    return Response({
        'success' :False,
        'message' : 'Invalid request !!',
        'data' : ''
    })
    

@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail(request, pk):
    """
    Retrieve, update or delete a code single_blog_data.
    """
    try:
        single_blog_data = BlogModel.objects.get(pk=pk)
    except BlogModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(single_blog_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogSerializer(single_blog_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        single_blog_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
def movie_view(request):
    get_model_data = Movie.objects.all()
    get_single_model_data = Movie.objects.get(id=2)
    director_name = get_single_model_data.director.name
    select_related_data = Movie.objects.select_related('director').all()[0].director
    all_director_name = Movie.objects.select_related('director').all().values('director__name')
    movies = Movie.objects.prefetch_related('director')
    movies_detail = Movie.objects.prefetch_related('director').values('id', 'movie_title', 'director')
    context = {
        'get_model_data': get_model_data,
        'get_single_data': director_name,
        'select_related_data': select_related_data,
        'all_director_name': all_director_name,
        'movies':movies,
        'movies_detail':movies_detail
        }
    return render(request,'model_data.html',context=context)
