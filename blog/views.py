from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Blog
from .forms import MyForm

from datetime import datetime as dt
import time



class Index(ListView):

    queryset = Blog.objects.all().filter(pk__gte = 2).order_by('-id')

    template_name = 'blog/blog_index.html'

    context_object_name = 'my_table'

    paginate_by = 3  # Display 10 objects per page

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context



class IndexForm(ListView):
    template_name = 'blog/index_form.html'
    form_class = MyForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})



class Detail(DetailView):

    model = Blog

    template_name = 'blog/blog_detail.html'

    context_object_name = 'my_table'


def run_process(request):
    if request.method == 'GET':
        name = request.GET['name']

        time = str(dt.now())
        res = name + '_' + time

        return JsonResponse({'time': res})


def dataTable(request):

    template_name = 'blog/dataTable.html'

    return render(request, template_name)


def check(request):

    template_name = 'blog/check.html'

    return render(request, template_name)
