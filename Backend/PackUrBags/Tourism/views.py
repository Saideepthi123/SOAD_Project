import jwt
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from Tourism.forms import RegistrationForm, AccountAuthenticationForm
from Tourism.models import UserData
from Tourism.utils import Util


def homepage(request):
    return render(request, 'homepage.html', {})


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            user = UserData.objects.get(username=username)
            user.id = user.user_id
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relative_link = reverse('email-verify')
            absurl = 'http://' + current_site + relative_link + "?token=" + str(token)
            email_body = 'Hi ' + user.username + ', click the link below to verify your email\n' + absurl
            message = {'email_body': email_body, 'email_subject': 'Verify your email', 'to_email': (user.email, )}
            Util.send_email(message)
            messages.success(request, f'Hello {username}, you are successfully registered. Check your {email} for verification link!')
            return redirect('login')
    form = RegistrationForm()
    return render(request, 'user_register.html', {'form': form})


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def verify_email(request):
    token = request.GET.get('token')
    secret_key = settings.SECRET_KEY
    try:
        payload = jwt.decode(token, secret_key)
        user = UserData.objects.get(user_id=payload['user_id'])
        if not user.is_verified:
            user.is_verified = True
            user.save()
            context = {
                'user': user,
                'status': 'successfully verified'
            }
            email_body = 'Your email was successfully verified. Thanks for registering.'
            message = {'email_body': email_body, 'email_subject': 'Welcome to PackUrBags', 'to_email': (user.email,)}
            Util.send_email(message)
            return render(request, 'verify_email.html', context=context)
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST, template_name='verify_email.html')
    except jwt.exceptions.DecodeError:
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST, template_name='verify_email.html')
    return Response({'error': 'Email not verified'}, status=status.HTTP_400_BAD_REQUEST, template_name='verify_email.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")

    else:
        form = AccountAuthenticationForm()

    return render(request, "user_login.html", {'login_form': form})
