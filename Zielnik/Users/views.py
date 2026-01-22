from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, UserProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  
            messages.success(request, f'Twoje konto zostało utworzone! Możesz się teraz zalogować, {username}!')  
            return redirect('login')
            
    else:
        # You might want to log the user in and redirect them after registration
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
     form_u = UserUpdateForm(request.POST, instance=request.user)
     form_p = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
     if form_u.is_valid() and form_p.is_valid():
         form_u.save()
         form_p.save()
         messages.success(request, f'Twoj profil zostal zaktualizowany!')
         return redirect('profile')
    else:
     form_u = UserUpdateForm(instance=request.user)
     form_p = UserProfileUpdateForm(instance=request.user.userprofile)

     context = {
         'form_u': form_u,
         'form_p': form_p
     }

     return render(request, 'Users/profile.html', context)

class UserLogoutView(LogoutView):
    http_method_names = ['get', 'post']
