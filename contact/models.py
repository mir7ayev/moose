from django.db import models
from config.base_models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=120)
    message = models.TextField()

    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
