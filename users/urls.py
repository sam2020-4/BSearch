from django.conf.urls import url
from BSproject.users import views as BSproject_views

urlpatterns = [    
    url(r'^signup/$', BSproject_views.signup, name='signup'),
]