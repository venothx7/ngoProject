from django.shortcuts import render, get_object_or_404
from register.models import Registration
from register.forms import RegisterForm
from event.models import Event
from register.models import Register

register = None
def register_create(request, event_id):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        event = get_object_or_404(Event, id=event_id)
        if form.is_valid():
            register = form.save()
            registration = Registration.create(Registration, event, event.adult_price,
                                                       event.child_price, register.adult_qty,
                                                       register.child_qty)
            return render(request, 'registers/register/totals.html', {'register': register,
                                                                      'event': event,
                                                                      'registration': registration})
    else:
        form = RegisterForm()
    return render(request, 'registers/register/create.html', {'form': form})


def confirm(request, register_id):
    register = get_object_or_404(Register, id=register_id)
    return render(request, 'registers/register/confirmation.html', {'register': register})






