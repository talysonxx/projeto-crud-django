from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    logout(request)
    
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)

            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)
