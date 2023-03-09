from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_index, name='post_index'),
    path('new', views.post_create, name='post_create'),
    path('post/<int:pk>', views.post_object, name='post_object')
]
