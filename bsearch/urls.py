from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [      
    url(r'^$', views.index, name= 'index'),
    url(r'^search/', views.search_donors, name='search_results'),
    url(r'^donor/(\d+)', views.get_donor, name='donor_results'),
    url(r'^new/donor$', views.new_donor, name='new-donor'),    
    url(r'^accounts/profile/$', views.user_profiles, name='profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
