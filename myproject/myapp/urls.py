# urls.py file of myapp

from django.urls import path
from . import views
app_name = 'myapp' # set the app_name attribute to your app name
urlpatterns = [
    path('', views.index, name='index'), # map the home page URL to index view
    path('create-post/', views.create_post, name='create_post'), # a URL pattern for the create post page that matches the create_post view

]
