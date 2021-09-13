from django.contrib.auth import forms
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from userauth.models import Training
from .forms import AddTrainingForm

import datetime

# Create your views here.
def index(request):
    return render(request, 'userauth/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password1'] 
            user = authenticate(username=username, password=password) 
            login(request, user) 
            return redirect('profile')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)

# You should consider caching the result of a request when the following cases are true:

#     rendering the page involves a lot of database queries and/or business logic,
#     the page is visited frequently by your users,
#     the data is the same for every user,
#     and the data does not change often.



def profile(request, duration):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddTrainingForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                form_obj = form.save(commit=False) # we have to use commit false to add the user
                form_obj.user = request.user
                form_obj.save()
            else:
                print("is not valid")
        current_user = request.user
        date_filter = False
        if request.method == 'GET':
            if duration != 999:
                date_filter = True
                current_date = datetime.date.today()
                requested_date = current_date - datetime.timedelta(days=duration)
                all_trainings_by_user = Training.objects.filter(
                    user=current_user, date__range=[requested_date, current_date]
                    ).order_by('date')
        if date_filter == False:
            all_trainings_by_user = Training.objects.filter(user=current_user).order_by('date')
        return render(request, 'userauth/profile.html', {
            'all_trainings_by_user': all_trainings_by_user,
            'user': current_user,
        })
    

    else: 
        return redirect('login')

def addTraining(request):
    form = AddTrainingForm()
    return render(request, "userauth/add_training.html", {'form': form})