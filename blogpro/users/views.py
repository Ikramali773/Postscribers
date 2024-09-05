from django.shortcuts import render, redirect
from .models import OTPModel
from .forms import SignupForm, UserUpdateForm, ProfileUpdateForm, LoginForm, OTPForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login
from django.contrib import messages
from django.core.mail import send_mail
from blogpro.settings import EMAIL_HOST_USER
import random
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.


def sign_up(request):
   
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            print("==============",form.cleaned_data)
            email=form.cleaned_data['email']
            check_user=User.objects.filter(email=email)
            if check_user:
                context={'message': 'Email already in use', 'class':'danger'}
                return render(request, 'users/sign_up.html', context)
            form.save()
            return redirect('users-login')
    else:
        form=SignupForm()

    return render(request, 'users/sign_up.html', {'form':form})


@login_required
def profile(request):
     if request.method=='POST':
        u_form=UserUpdateForm(request.POST or None, instance=request.user )
        p_form=ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
          
     else:
          u_form=UserUpdateForm(instance=request.user)
          p_form=ProfileUpdateForm( instance=request.user.profilemodel)

     context={
          'u_form':u_form,
          'p_form':p_form
     }
     return render (request, 'users/profile.html', context)

def login_view(request):
    
    if request.method=='POST':
       form=LoginForm(request.POST)
       if form.is_valid():
           email=request.POST.get('email')
        #    user=User.objects.raw(f"Select username from public.auth_user where email={u_email}")
           user=User.objects.filter(email = email).first()
           if user is None:
                context={'message':'User Not Found'}
                return render (request, 'users/login.html', context)
           otp_user=OTPModel.objects.filter(user=user).first()
           
           if otp_user:
            
            otp=str(random.randint(10000, 99999))
            otp_user.otp=otp
            
            otp_user.otp_time= timezone.now() 
            otp_user.save()

            send_mail('Your OTP', f'Here is your OTP: {otp}. This will Expire in 5 minutes', EMAIL_HOST_USER, [email], fail_silently=False )
            request.session['email'] = email
            return redirect ('otp')
           else:
                otp_user=OTPModel.objects.create(user=user)
                otp=str(random.randint(10000, 99999))
                otp_user.otp=otp
            
                otp_user.otp_time= timezone.now() 
                otp_user.save()

                send_mail('Your OTP', f'Here is your OTP: {otp}. This will Expire in 5 minutes', EMAIL_HOST_USER, [email], fail_silently=False )
                request.session['email'] = email
                return redirect ('otp')
           
    form=LoginForm()
    return render(request, 'users/login.html', {'form':form})

def otp(request): 
    form=OTPForm()
    email=request.session['email']
    if request.method=='POST':
        form=OTPForm(request.POST)
        user=User.objects.filter(email=email).first()
        otp_user=OTPModel.objects.filter(user=user).first()
        if form.is_valid():
           
            
            otp=form.cleaned_data['otp']
            if otp == '':
                return render(request, 'users/otp.html', {'message':'Invalid OTP', 'class': 'danger'})
           
            
            check_otp=OTPModel.objects.filter(otp=otp).exists()

            if otp_user.otp_time - timezone.now()>timedelta(minutes=5):
                return render(request, 'users/otp.html', {'message':'OTP Expired', 'class': 'danger'})
            if check_otp :
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'users/otp.html', {'message':'Wrong OTP', 'class': 'danger'})
    return render (request, 'users/otp.html', {'form':form})

def resend_otp(request):
    email=request.session['email']
    user=User.objects.filter(email=email).first()
    otp_user=OTPModel.objects.filter(user=user).first()


    otp=str(random.randint(10000, 99999))
    otp_user.otp=otp
    otp_user.otp_time= datetime.now() 
    otp_user.save()

    send_mail('Your OTP', f'Here is your OTP: {otp}. This will Expire in 5 minutes', EMAIL_HOST_USER, [email], fail_silently=False )
    request.session['email'] = email
           
    return redirect('otp')