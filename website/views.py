from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Team_A_Member

def home(request):
	records = Team_A_Member.objects.all()


	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "OO IKAW PARIN")
			return redirect('home')
		else:
			messages.success(request, "HINDI IKAW")
			return redirect('home')

	else:
		return render(request, 'home.html', {'records':records})


def logout_user(request):
	logout(request)
	messages.success(request, "HINDI KABA NANINIWALA SA RED STRING THEORY")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "HINDI MO SIYA MAPAPANTAYAN")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def team_a_record(request, pk):
	if request.user.is_authenticated:
			#Look Up Records
			team_a_record = Team_A_Member.objects.get(id=pk)
			return render(request, 'record.html', {'team_a_record':team_a_record})
	else:
		messages.success(request, "HINDI KA TEAM A MEMBER")
		return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Team_A_Member.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "BAKIT MO BINURA")
		return redirect('home')
	else:
		messages.success(request, "HINDI KA TEAM A MEMBER")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "BUTI NAMAN NAGLAGAY KANA")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "HINDI KA TEAM A MEMBER")
		return redirect('home')	

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Team_A_Member.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "NAUPDATE NA BEETCH")
			return redirect('home')	
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "HINDI KA TEAM A MEMBER")
		return redirect('home')	