from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from uritemplate import partial
from blogs.serializers import  BlogSerializer
from blogs.models import BlogModel

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
