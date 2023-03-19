from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def base(request):
    return render(request, 'app/base.html')

def immunization(request):
    return render(request, 'app/immunization.html')

def health(request):
    return render(request, 'app/health.html')

def economic(request):
    return render(request, 'app/economic.html')

def mortality(request):
    return render(request, 'app/mortality.html')

def social(request):
    return render(request, 'app/social.html')

def about(request):
    return render(request, 'app/about.html')





