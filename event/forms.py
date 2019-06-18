from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name',
                  'description',
                  'category',
                  'start_date',
                  'end_date',
                  'start_time',
                  'end_time',
                  'location',
                  'register',
                  'image',
                  'location',
                  'adult_price',
                  'child_price',
                  )