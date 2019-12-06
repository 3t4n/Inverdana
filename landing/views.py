from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def inverdana_site(request):
    return render(request, 'blog.html')

#def docs(request):
#    return render(request, 'documentation.html')

#def api(request):
#    return render(request, 'infoapi.html')
