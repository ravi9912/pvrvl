from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
#from .models import userprofile
import datetime 
import random
import smtplib
from django.core.mail import EmailMessage
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def homepage(request):
	return render(request,"home/home.html")
def login(request):
	if request.method == 'POST':
	
		request.session["uname"] = request.POST['e']
		request.session["password"] = request.POST['p']
		
		userd =auth.authenticate(request,username=request.session["uname"],password=request.session["password"])
		if userd is not None:
			
			u = User.objects.get(username=request.session["uname"])
			
			otp = random.randrange(111111, 999999)
			request.session["o"] = otp
			
			email = EmailMessage()
			email.subject = 'PVRVL OTP'
			email.body = str(otp)
			email.from_email = 'pvrvlotp@gmail.com'
			email.to = [u.email]
			email.send()

			return redirect('home:otp_verification')

		else:
			messages.warning(request,'inavalid details,')
			return render(request,'home/login.html',{'password':request.session["password"],'username':request.session["uname"]})

	else:
		return render (request,'home/login.html')


def otp_verification(request):
	if request.method=='POST':
		request.session["o2"] = int(request.POST['otp1'])
		userd =auth.authenticate(request,username=request.session["uname"],password=request.session["password"])
		if request.session["o2"] == request.session["o"]:
			auth.login(request,userd)
			return redirect("home:homepage")

		else:
			messages.warning(request,'enter correct otp') 
			return render(request,'home/otp.html')
	else:
		return render(request,'home/otp.html')


@login_required	
def logout(request):
	auth.logout(request)
	return redirect("home:mainmenu")


@login_required
def create_new_user(request):
	if request.method == 'POST':
		user_name = request.POST.get('usrname')
		password = request.POST.get('psw')
		email = request.POST.get('email')

		if User.objects.filter(username=user_name):
			messages.warning(request,'User name Already Taken') 
			return render(request,"home/create_new_user.html",{'u':user_name,'e':email,'p':password})
		elif User.objects.filter(email=email):
			messages.warning(request,'Email Already Registred')
			return render(request,"home/create_new_user.html",{'u':user_name,'e':email,'p':password})
		else:
			user = User.objects.create_user(username=user_name,email=email,password=password)
			messages.info(request,'User Created Successfully...')
			return render(request,"home/create_new_user.html")

	else:
		return render (request,'home/create_new_user.html')


def mainmenu(request):
    return render(request, 'home/mainmenu.html', {})


@login_required
@staff_member_required
def masterlogin(request):
	if request.method == 'POST':

		#user = authenticate(request, username=request.POST['username'],password='Ravi@1234')
		user = request.POST['username']
		#if user is not None:
		users = User.objects.filter(username=user)
		for u in users:
			auth.login(request,u)
			return redirect('home:homepage')

		else:
			messages.warning(request,'inavalid details,')
			return render(request,'home/login_as_user.html')
	else:
		return render (request,'home/login_as_user.html')

'''def fgpassword(request):
	return render(request,'forgot.html')

@login_required	
def calculator(request):
    return render(request, 'home/calculator.html', {})'''