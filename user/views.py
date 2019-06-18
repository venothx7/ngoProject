from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from django.views import generic
from .models import User
from .forms import UserForm

class Index(generic.ListView):
    model = User
    context_object_name = 'users'
    template_name = 'user/userlist.html'

class UserCreateView(BSModalCreateView):
    template_name = 'user/user_create.html'
    form_class = UserForm
    success_message = 'Success: User was created.'
    success_url = ('/user/')


class UserUpdateView(BSModalUpdateView):
    model = User
    template_name = 'user/user_create.html'
    form_class = UserForm
    success_message = 'Success: User was updated.'
    # queryset = User.objects.all()
    success_url = ('/user/')


class UserDelete(BSModalDeleteView):
    model = User
    template_name = 'user/user_delete.html'
    success_message = 'Success: User was deleted.'
    success_url = ('/user/')



