from django.shortcuts import render, redirect
from django.contrib import messages, auth
# from django.contrib.auth.models import User  # noqa
from django.contrib.auth import get_user_model


User = get_user_model() # εισαγωγη από το core διοτι εχω κανει αλλαγες εκει σε σχεση με τα defaults.


def register(request):
    """Docstring"""
    if request.method == 'POST':
        #  Get form values
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password match
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            else:
                # All OK
                user = User.objects.create_user(email=email, )
                # Login right after register
                # auth.login(request, user)
                # messages.success(request, "You are logged in")
                # return redirect('index')

                # Login manually
                user.save()
                messages.success(request, "You are now registered and can proceed to log in")
                return redirect('login')
        else:
            messages.error(request, 'Passwords must match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    """Docstring"""
    if request.method == 'POST':
        #  Login User
        pass
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    """Docstring"""
    return redirect('index')


def dashboard(request):
    """Docstring"""
    return render(request, 'accounts/dashboard.html')
