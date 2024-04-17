from django.db import models
from config.base_models import BaseModel
from django.contrib.auth.models import User


class PostTags(BaseModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')

    tags = models.ManyToManyField(PostTags)
    description = models.TextField()

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.name
