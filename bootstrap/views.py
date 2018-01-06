from django.shortcuts import render

# Create your views here.


def grid_layout(request):
    template_name = 'bootstrap/grid_layout.html'

    return render(request, template_name)


def toggle_button(request):
    template_name = 'bootstrap/toggle_button.html'

    return render(request, template_name)


def modal(request):
    template_name = 'bootstrap/modal.html'

    return render(request, template_name)


def form(request):
    template_name = 'bootstrap/form.html'

    return render(request, template_name)


def thumnail(request):
    template_name = 'bootstrap/thumnail.html'

    return render(request, template_name)


def jquery(request):
    template_name = 'bootstrap/jquery.html'

    return render(request, template_name)
