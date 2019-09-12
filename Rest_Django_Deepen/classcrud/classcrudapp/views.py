from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ClassBlog


# Create your views here.

class BlogView(ListView):
    # html with blog list information
    # default html name value = (small letter model)_list.html
    # template_name = 'classcurdapp/list.html' set html name value / default -> custom
    # context_object_name = 'blog_list' 매인 디폴트 object 이름 변경
    model = ClassBlog


class BlogCreate(CreateView):
    # html with form(input space) information
    # default html name value = (small letter model)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')


class BlogDetail(DetailView):
    # html with detail page information
    # default html name value = (small letter model)_detail.html
    # context_object_name = 'blog_detail' detail 에서 object 이름 변경
    model = ClassBlog


class BlogUpdate(UpdateView):
    # html with form(input space) information
    # default html name value = (small letter model)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')


class BlogDelete(DeleteView):
    # html with "is really want delete?" information
    # default html name value = (small letter model)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')

