from email.policy import default
from cloudinary.models import CloudinaryField
from django.db import models


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
         'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
        )
    body = models.CharField(
    'body', blank=True, null=True, max_length=140, db_index=True
    )
    image = CloudinaryField(
        'image', blank=True, db_index=True
    )
    like = models.IntegerField(
        blank= True, default= 0
    )
    created_at = models.DateTimeField(
    'Created DateTime', blank=True, auto_now_add=True
    )
    
    