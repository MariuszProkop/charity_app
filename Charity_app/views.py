from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from Charity_app.models import Institution, Donation, Category


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
            'organizacje': organizacje})


class AddDonationView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        category = Category.objects.filter(institution=None)
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'category': category,
                                             'institutions': institutions})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class ConfirmationView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


@login_required
def user_profile(request):
    return render(request, 'user_profile.html')
