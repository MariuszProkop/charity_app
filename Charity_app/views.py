from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from Charity_app.models import Institution, Category, Donation


class LandingPageView(View):
    def get(self, request):
        institutions = Institution.objects.all()

        institution_count = Institution.objects.count()
        total_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
        category = Category.objects.all()
        return render(request, 'index.html', {'institutions': institutions, 'category': category,
                                              'institution_count': institution_count, 'total_bags': total_bags})


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/'

class ConfirmationView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')
