from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context)
