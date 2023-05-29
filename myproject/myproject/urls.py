# urls.py file of myproject

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('myapp.urls')), # include the URLs of myapp app
    path('', include('myapp.urls')), # include the URLs from your app under the blog namespace
]
