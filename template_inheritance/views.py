from django.shortcuts import render

# Create your views here.


def index(request):
    template_name = 'template_inheritance/child.html'

    return render(request, template_name)


def base(request):
    template_name = 'template_inheritance/base.html'

    return render(request, template_name)
