from django.shortcuts import render

# Create your views h

def Filter(request):
    return render(request, 'custom/index.html')


def form(request):
    return render(request, 'custom/form.html')