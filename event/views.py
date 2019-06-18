from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Event
from .forms import EventForm

# Create your views here.

def index(request):
    # posts = Posts.objects.all()[:10]
    events = Event.objects.all
    context = {
        'events': events
    }
    return render(request, 'event/event_list.html', context)
class Index(generic.ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event/event_list.html'

class EventCreateView(CreateView):
    template_name = 'event/event_create.html'
    success_url = '/event'
    form_class = EventForm
    success_message = 'Success: Book was created.'


class EventUpdateView(UpdateView):
    # template_name = 'user/user_create.html'
    template_name = 'event/event_create.html'
    queryset = Event.objects.all()
    success_url = '/event'
    success_message = 'Success: Book was updated.'
    form_class = EventForm


class EventDelete(DeleteView):
    model = Event
    template_name = 'event/event_delete.html'
    success_url = ('/event')
    success_message = 'Success: Book was deleted.'