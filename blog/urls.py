from django.urls import path

from .views import *


urlpatterns = [
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('cetegory/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('', Home.as_view(), name='home'),

]
