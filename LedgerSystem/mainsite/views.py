from django.shortcuts import render

# Create your views here.
def createXlsx(request):
    if request.method == 'GET':
        return render(request, 'createXLX.html', context)
