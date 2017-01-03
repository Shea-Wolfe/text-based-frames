from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


regster_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                user = authenticate(username=user.username,
                                    password=request.POST['password1'])
                login(request, user)
                #Send the user to a game here
    else:
        form = UserCreationForm()
    return render(request, 'text_games/register.html', {'form':form}) 
