from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('post/', views.post_list, name='post_list'),
    path('contact/', views.contact_view, name='contact'),
]
