from django.conf.urls import url
from tutorial.users import views as tutorial_views

urlpatterns = [
    
    url(r'^signup/$', neighbour_views.signup, name='signup'),
]