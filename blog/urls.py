from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cetegory/<str:slug>/', get_category, name='category'),
    path('post/<str:slug>/', get_post, name='post'),
]

