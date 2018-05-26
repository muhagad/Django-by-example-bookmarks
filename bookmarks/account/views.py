from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            # if user has a value to authenticate
            if user is not None:
                # Let's check to see if i have a record in my database of that user
                if user.is_active:
                    login(request, user)
                    return HttpResponse('<h2>Authenticated successfully</h2>')
                else:
                    return HttpResponse('<h2>Disabled account</h2>')
            else:
                return HttpResponse('<h2>Invalid Login</h2>')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})






