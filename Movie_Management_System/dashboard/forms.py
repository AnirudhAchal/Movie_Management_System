from django import forms
from django.contrib.auth.models import User
from .models import Booking,Show

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('number_of_seats', 'show')

        def __init__(self,movie_id,*args, **kwargs):
            bruhhh,fuck,this,shit,lmao
            super(BookingForm, self).__init__(*args, **kwargs)
            self.fields['show'].queryset = Show.objects.get(movie_id=movie_id)

