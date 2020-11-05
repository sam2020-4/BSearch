from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

# Create your models here.
# COUNTY class
class County(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)    

    def save_county(self):
        self.save()
    
    def delete_county(self):
        self.delete()
        
    @classmethod
    def get_countys(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_countys(cls, search_term):
        projects = cls.objects.filter(name__icontains=search_term)
        return projects    
    
    @classmethod
    def get_by_admin(cls, Admin):
        projects = cls.objects.filter(Admin=Admin)
        return projects    
    
    @classmethod
    def get_county(request, county):
        try:
            project = County.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My County'
        verbose_name_plural = 'Countys'

# profile class
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = CloudinaryField('profile_pics/', blank=True)
    county = models.ForeignKey(County,on_delete=models.CASCADE, blank=True, default='1')

    def save_profile(self):
        self.save()         

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return f"{self.user}, {self.bio}, {self.photo}"
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

       
class Donor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    admin_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    address = models.TextField()
    county = models.ForeignKey(County,on_delete=models.CASCADE, blank=True, default='1')
    police_cont = models.CharField(max_length=255)
    health_cont = models.CharField(max_length=255)

   
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
        
    @classmethod
    def get_allbusiness(cls):
        business = cls.objects.all()
        return business
    
    @classmethod
    def search_business(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business
    
    @classmethod
    def get_by_neighborhood(cls, neighborhoods):
        business = cls.objects.filter(neighborhood__name__icontains=neighborhoods)
        return business
    
    @classmethod
    def get_businesses(request, id):
        try:
            business = Business.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return business
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Business'
        verbose_name_plural = 'Business'


