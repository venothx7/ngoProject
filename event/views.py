from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic

from .models import Event
from .forms import EventForm


def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper

@superuser_required()
class Index(LoginRequiredMixin, generic.ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event/event_list.html'

@superuser_required()
class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = 'event/event_create.html'
    success_url = '/event'
    form_class = EventForm
    success_message = 'Success: Book was created.'

@superuser_required()
class EventUpdateView(LoginRequiredMixin, UpdateView):
    # template_name = 'user/user_create.html'
    template_name = 'event/event_create.html'
    queryset = Event.objects.all()
    success_url = '/event'
    success_message = 'Success: Book was updated.'
    form_class = EventForm

@superuser_required()
class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'event/event_delete.html'
    success_url = ('/event')
    success_message = 'Success: Book was deleted.'


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/list.html', {'events': events})


def register_detail(request, id, slug):
    event = get_object_or_404(Event, id=id, slug=slug)
    print("got here")
    return render(
        request,
        'event/register_detail.html',
        {'event': event})
