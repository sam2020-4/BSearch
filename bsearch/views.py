from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from users.models import Profile


# Create your views here.
# @login_required(login_url='/login/')
def index(request):
    # neighbourhoods = Neighbourhood.objects.all()
    
    return render(request, 'index.html')

    
