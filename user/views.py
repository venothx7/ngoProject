from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from .models import CustomUser
from .forms import UserForm, SignupForm



def login_success(request):
    print(request.user.is_superuser)
    print("HELO!!!")
    if request.user.is_superuser:
        return redirect('/user')
    else: 
        # redirect them
        return redirect ('/event/userview')
    return redirect('/user')

class SignUp(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_message = 'Success: User was created.'
    success_url = ('../login')

def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper

@superuser_required()
class Index(LoginRequiredMixin , generic.ListView):
    
    model = CustomUser
    context_object_name = 'users'
    template_name = 'user/userlist.html'

@superuser_required()
class UserCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'user/user_create.html'
    form_class = UserForm
    success_message = 'Success: User was created.'
    success_url = ('/user/')

@superuser_required()
class UserUpdateView(BSModalUpdateView):
    model = CustomUser
    template_name = 'user/user_create.html'
    form_class = UserForm
    success_message = 'Success: User was updated.'
    # queryset = User.objects.all()
    success_url = ('/user/')

@superuser_required()
class UserDelete(BSModalDeleteView):
    model = CustomUser
    template_name = 'user/user_delete.html'
    success_message = 'Success: User was deleted.'
    success_url = ('/user/')



