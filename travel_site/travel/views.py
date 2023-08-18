from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from travel.forms import AddTripForm, SignUpForm
from travel.models import Travel

User = get_user_model()


def index(request):
    return render(request, "travel/index.html")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_travel')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    else:
        form_signup = SignUpForm()
        form_login = AuthenticationForm()
        context = {'form_signup': form_signup, 'form_login': form_login}
        return render(request, 'travel/login.html', context)
    

def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_travel')
    else:
        form = SignUpForm()
    return render(request, 'travel/travel_list.html', {'form': form})


def list_travel(request):
    my_travels = Travel.objects.filter(planned_by=request.user)    
    joined_travels = Travel.objects.filter(users_joining=request.user)
    my_combined_travels = my_travels | joined_travels
    others_travels = Travel.objects.exclude(pk__in=my_combined_travels.values('id'))

    return render(request, "travel/travel_list.html", {'travels': my_combined_travels, 'others_travels': others_travels})




def detail_travel(request, pk):
    travel = Travel.objects.get(pk=pk)
    context = {'travel': travel}
    return render(request, 'travel/travel_detail.html', context)


def add_travel(request):
    form = AddTripForm()
    
    if request.method == 'POST':
        form = AddTripForm(request.POST)

        if form.is_valid():
            travel_data = form.cleaned_data
            travel_data['planned_by'] = request.user
            new_travel = Travel.objects.create(**travel_data)
        
        return redirect('list_travel')
    
    return render(request, "travel/add_travel.html", {'form': form})


def join_travel(request, pk):
    travel = Travel.objects.get(pk=pk)
    if request.user not in travel.users_joining.all():
        travel.users_joining.add(request.user)
    return redirect('list_travel')