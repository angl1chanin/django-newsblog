from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import messages

from accounts.models import User
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('news:home')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        super().form_valid(form)
        login(self.request, self.object)
        return redirect('news:home')


class SignInView(LoginView):
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('news:home')
    template_name = 'accounts/signin.html'

    def post(self, request, *args, **kwargs):
        super(SignInView, self).post(self, request, *args, **kwargs)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('news:home')
        else:
            messages.error(request, 'username or password doesn\'t exist')
            return redirect('accounts:signin')
