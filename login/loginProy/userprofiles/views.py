from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def authentication(request):
	if request.method == 'POST':
		action = request.POST.get('action', None) #toma los valores enviados por el metodo post
		username = reques.POST.get('username', None)
		password = reques.POST.get('password', None)

		if action == 'signup':
			user = User.objects.create_user(username = username, password = password)
			user.save()
		elif action == 'login':
			user = authenticate(username = username, password = password)
			login(request, user)

	return render(request, 'login.html', {})
