from django import forms
from .models import Reservation
from django.core.mail import send_mail

class ReservationTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        labels = {
            'person_num': ('Person'),
        }
        help_texts = {
            'name': ("Enter your full name"),
        }
        widgets = {'date': forms.DateInput(
            format=('%m/%d/%Y'),
            attrs={'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'}
            )
            },

class ContactForm(forms.Form):
    subject = forms.CharField()
    from_email = forms.EmailField(required = True)
    message = forms.CharField(widget=forms.Textarea ,  required = True)

    def send_email(self):
        subject = self.cleaned_data['subject']
        email = self.cleaned_data['from_email']
        message = self.cleaned_data['message']

        send_mail(
            subject,
            message,
            email,
            ['b999086@gmail.com'],
            fail_silently=False
        )
