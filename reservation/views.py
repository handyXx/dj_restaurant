from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, FormView, TemplateView
from .forms import ReservationTableForm, ContactForm
from django.views.generic.edit import FormMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy

class ReservationView(FormView):
    template_name = "reservation/reservation.html"
    form_class = ReservationTableForm

class ContactView(FormView):
    template_name = "reservation/contact.html"
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)                 #HttpResponseRedirect(reverse_lazy('contact'))
