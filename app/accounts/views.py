from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
# from django.contrib.auth.models import User  # noqa
from django.contrib.auth import get_user_model


# εισαγωγη από το core διοτι εχω κανει αλλαγες εκει σε σχεση με τα defaults.
User = get_user_model()


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
                user = User.objects.create_user(
                    email=email,
                    password=password
                )
                # Login right after register
                # auth.login(request, user)
                # messages.success(request, "You are logged in")
                # return redirect('index')

                # Login manually
                user.save()
                messages.success(
                    request,
                    "You are now registered and can proceed to log in"
                )
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
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(
            email=email,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    """Docstring"""
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboard(request):
    """Docstring"""
    return render(request, 'accounts/dashboard.html')
