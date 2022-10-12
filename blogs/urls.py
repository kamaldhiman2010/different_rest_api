
from django.contrib import admin
from django.urls import path
from blogs.views.class_based_view_using_apiviews import BlogAPIView

from blogs.views.fn_based_views import blog_detail, blog_view
from blogs.views.generic_api_views import BlogCreateView, BlogListCreateAPI, BlogListView, BlogRetriveUpdateDestroyAPI
from blogs.views.viewsets_api_views import BlogViewSets, BlogModelViewSets


urlpatterns = [
    path('cbv/', blog_view),
    path('cbv/<int:pk>/', blog_detail),
    path('apiviews/', BlogAPIView.as_view()),
    path('generics/', BlogListCreateAPI.as_view()),
    path('generics_list/', BlogListView.as_view()),
    path('generics_create/', BlogCreateView.as_view()),


    path('generics/<int:pk>/', BlogRetriveUpdateDestroyAPI.as_view()),
    path('viewsets/', BlogViewSets.as_view({'get': 'list'}), name='blog-list'),
    path('viewsets/<int:pk>/',BlogViewSets.as_view({'get': 'retrieve'}), name='blog-detail'),
    # modelviewset
    path('model_viewsets/',BlogModelViewSets.as_view({'get': 'list'})),
    path('create_viewsets/', BlogModelViewSets.as_view({'post': 'create'})),
    path('update_viewsets/<int:pk>/', BlogModelViewSets.as_view({'put': 'update'})),
    path('delete_viewsets/<int:pk>/', BlogModelViewSets.as_view({'delete': 'destroy'})),
    path('model_viewsets/<int:pk>/', BlogModelViewSets.as_view({'get': 'retrieve'}))


]
