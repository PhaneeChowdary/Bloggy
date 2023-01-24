from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()    #Unristricted text (means you can write any no of lines)
    date_posted = models.DateTimeField(default=timezone.now)
    #"auto_now_add=True" in DateTimeField will be updated only once i.e., when post is created, because if date_posted change after every time you modify the content then original publication date will be overwritten.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pk': self.pk})