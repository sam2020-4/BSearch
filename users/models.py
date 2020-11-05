from django.db import models
from django.contrib.auth.models import User
import cloudinary.uploader
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, default="I love learning,it is a source of inspiration", blank=True)
    image = cloudinary.models.CloudinaryField('profile_pics')
    neighbourhood = models.CharField(max_length=25, default="kitengela", blank=True)
    Location = models.CharField(max_length=25, default="Nairobi", blank=True)
        
    def save_profile(self):
        self.save()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

