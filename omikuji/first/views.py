from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'first/main.html')


def definition (request):
    return render(request,'first/definition.html')


def fortune (request):
    return render(request,'first/fortune.html')


def daegil (request):
    return render(request,'first/daegil.html')


def gil (request):
    return render(request,'first/gil.html')


def sogil (request):
    return render(request,'first/sogil.html')


def margil (request):
    return render(request,'first/margil.html')


def hyung (request):
    return render(request,'first/hyung.html')