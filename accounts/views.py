from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from accounts.models import Account, Farmer
from logs.models import *


# Create your views here.
@login_required(login_url='signin')
def home(request):
	farmer = Farmer.objects.all()
	logs = Harvest_Logs.objects.all()
	return render(request, 'index.html', {'farmer': farmer, 'logs': logs})

def signup(request):
	if request.method == 'POST':
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		if Account.objects.filter(email=email):
			messages.error(request, 
				'Email Address already exists. Try with a different Email Address.')
		if pass1 != pass2:
			messages.error(request, 
				'Passwords do not match! Try again.')

		newuser = Account.objects.create_user(email=email, password=pass1)
		newuser.save()
		messages.success(
			request, 'Account Successfully Created.')

		user = authenticate(email=email, password=pass1)

		login(request, user)

		return redirect('CompleteSignup')

	return render(request, 'accounts/signup.html')

def CompleteSignup(request):
	if request.method == 'POST':
		First_Name = request.POST['Fname']
		SurName    = request.POST['Surname']
		Farm_ID    = request.user
		ID_Number  = request.POST['ID_No']
		Phone_No   = request.POST['Phone_No']
		Farm_Name  = request.POST['Farm_Name']

		userInfo = Farmer.objects.create(First_Name=First_Name, SurName=SurName, Farm_ID=Farm_ID, ID_Number=ID_Number, Phone_No=Phone_No, Farm_Name=Farm_Name)
		userInfo.save()
		messages.success(request, 'Successful!')

		return redirect('home')

	return render(request, 'accounts/CompleteSignup.html')

def signin(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['pass1']

		user = authenticate(email=email, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, 'Login Successful.')
			return redirect('home')
		else:
			messages.error(request, 'Bad Credentials!')
			return redirect('signin')

	return render(request, 'accounts/login.html')

def signout(request):
	logout(request)
	messages.success(request, "Logged out")
	return redirect("signin")
