from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.conf import settings
from django.core.mail import send_mail

from App_Login.models import *
from App_Login.forms import ProfileForm, SignUpForm, UserProfileChange

from django.contrib import messages
import razorpay
import uuid

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def register_attempt(request):

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        contact = request.POST.get('contact')
        occupation = request.POST.get('occupation')
        organization = request.POST.get('organization')
        question = request.POST.get('question')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(fullname)

        # print(gender)
        print(contact)


        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return HttpResponseRedirect(reverse('App_Login:register_attempt'))

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return HttpResponseRedirect(reverse('App_Login:register_attempt'))




            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token, fullname = fullname, contact=contact, occupation=occupation, organization=organization, question=question)
            profile_obj.save()
            # html_content = render_to_string("email_template.html",{'username':username,'password':password})
            # text_content = strip_tags(html_content)
            #
            # email_send = EmailMultiAlternatives(
            #     "ICFC Confirmation Email",
            #     text_content,
            #     settings.EMAIL_HOST_USER,
            #     [email],

            # email_send.attach_alternative(html_content,"text/html")
            # email_send.send()
            # print(email_send)
            return HttpResponseRedirect(reverse('App_Login:login_attempt'))


        except Exception as e:
            print(e)


    return render(request , 'App_Login/register.html')

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return HttpResponseRedirect(reverse('App_Login:login_attempt'))

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return HttpResponseRedirect(reverse('App_Login:login_attempt'))

        login(request , user)
        return HttpResponseRedirect(reverse('home'))

    return render(request , 'App_Login/login.html')

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request,"You Are Logged Out!")
    return HttpResponseRedirect(reverse('home'))
