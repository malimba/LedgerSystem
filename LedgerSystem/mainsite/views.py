from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    if request.method == 'GET':
        serviceObjs = Service.objects.all()
        context = {'serviceOpts':serviceObjs}
        return render(request, 'home.html', context)
