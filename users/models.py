from django.db import models
import uuid

# Create your models here.

class Users(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    profile_img = models.TextField()
    registered_diecasts = models.IntegerField(blank=False, null=False, default=0)
    birth_date = models.DateField()
    created_at = models.DateTimeField(null=False, blank=False)       
    
    
