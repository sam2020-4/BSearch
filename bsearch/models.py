from django.db import models

# Create your models here.
# profile class
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = CloudinaryField('profile_pics/', blank=True)
    county = models.ForeignKey(County,on_delete=models.CASCADE, blank=True, default='1')

    def save_profile(self):
        self.save()
        
        # img = Image.open(self.photo.path)
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.photo.path)            

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return f"{self.user}, {self.bio}, {self.photo}"
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
