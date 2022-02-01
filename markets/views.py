from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'cmpx/index.html')

def programs(request):
    return render(request, 'cmpx/programs.html')