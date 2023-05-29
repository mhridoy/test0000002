
from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect
from django.utils import timezone

def index(request): # a view for the home page
    posts = Post.objects.all() # get all posts from the database
    context = {'posts': posts} # create a context dictionary to pass data to the template
    return render(request, 'index.html', context) # render a template with the context

def create_post(request): # a view for creating a new post
    if request.method == 'POST': # check if the request is a POST request
        title = request.POST['title'] # get the title value from the form
        content = request.POST['content'] # get the content value from the form
        #author = request.user # get the current user as the author
        created_at = timezone.now() # get the current date and time as the creation date
        post = Post(title=title, content=content, created_at=created_at) # create a new Post instance with the values
        post.save() # save the Post instance to the database
        return redirect('/') # redirect to the home page
    else: # if not a POST request, render an empty form
        return render(request, 'create_post.html')
