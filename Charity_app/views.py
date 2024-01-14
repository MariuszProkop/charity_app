from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView


from Charity_app.models import Institution, Category, Donation


class LandingPageView(View):
    def get(self, request):
        institutions = Institution.objects.all()

        institution_count = Institution.objects.count()
        total_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0

        fundacje = institutions.filter(type='fundacja')
        zbiorki_lokalne = institutions.filter(type='zbiorka_lokalna')
        organizacje = institutions.filter(type='organizacja_pozarzadowa')

        return render(request, 'index.html', {
            'institutions': institutions,

            'institution_count': institution_count,
            'total_bags': total_bags,
            'fundacje': fundacje,
            'zbiorki_lokalne': zbiorki_lokalne,
            'organizacje': organizacje,})

class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class ConfirmationView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')
