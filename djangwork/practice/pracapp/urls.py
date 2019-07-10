from django.conf.urls import url
from django.urls import path
from pracapp.views import post_list
from pracapp.views import post_detail
from pracapp.views import new_post

urlpatterns = [
    url('^$', post_list, name ='post_list'),
    path('pracapp/<int:pk>/', post_detail, name='post_detail'),
    path('pracapp/new/', new_post, name='post_new'),
]