from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Student
from .forms import Regno
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login/")
def home(request):
	if request.method == 'POST':
		form = Regno(request.POST)
		if form.is_valid():
			selected_reg = Student.objects.filter(regno=request.POST.get('regno'))
			return render(request, 'home.html',{'selected_reg': selected_reg,'form':form})
	else:
		form = Regno()

	return render(request, 'home.html', {'form': form})

