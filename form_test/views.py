from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect


# Create your views here.

def index(request):
    template_name = 'form_test/index.html'

    return render(request, template_name)


def form_action(request):
    template_name = 'form_test/form_action.html'

    if request.method == 'GET':
        context = request.GET

    return render(request, template_name, context)


def login_check(request):

    request.session['set_value'] = '123456'

    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            return redirect('form_action')


def dropdown(request):
    template_name = 'form_test/dropdown.html'

    return render(request, template_name)
