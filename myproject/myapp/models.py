from django.db import models
from django.contrib.auth.models import User

class Post(models.Model): # a model for blog posts
   # author = models.ForeignKey(User, on_delete=models.CASCADE) # define the author field
    title = models.CharField(max_length=100) # a character field for the title
    content = models.TextField() # a text field for the content
    created_at = models.DateTimeField(auto_now_add=True) # a date-time field for the creation date

    def __str__(self):
        return self.title # a string representation of the model
