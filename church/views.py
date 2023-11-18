from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from datetime import datetime
from .models import CustomUser
from .models import Donation
from .models import Message
from .models import Event
from .forms import CustomUserCreationForm, EventForm, DonationForm,MessageForm,CustomUserUpdateForm


# Create your views here.
def home(request):
    return render(request, 'main.html', {})

def loginUser(request):
    page ='login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method =='POST' :
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
          login(request,user)
          return redirect('home')
        else:
            print(request, 'Username OR password is incorrect')
    return render(request, 'church/login-register.html')

def registerUser(request):
    page ='register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request,user)
            return redirect('home')

        else:
            pass
    context ={'page': page,'form': form}
    return render(request,'church/login-register.html', context)
@login_required
def logoutUser(request):
    logout(request)
    return redirect ('login')

@login_required
def upcoming_events(request):
    today = datetime.today()
    upcoming_events = Event.objects.filter(date__gte=today).order_by('date')
    return render(request, 'church/upcoming_events.html', {'upcoming_events': upcoming_events})

@login_required
def donations(request):
    donations = Donation.objects.all()
    context = {'donations':donations}
    return render(request,'church/donations.html', context)

@login_required
def messages(request):
    user =request.user
    messages=Message.objects.filter(recipient=user)
    context = {'messages':messages}
    return render(request,'church/messages.html',context)

@login_required
def updateProfile(request, pk):
    profile = CustomUser.objects.get(id=pk)
    form = CustomUserUpdateForm(instance=profile)
    
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST or None, instance=profile)
        if form.is_valid():
            form.save()
            login(request, profile)
            return redirect('home')
    else:
        form = CustomUserUpdateForm(instance=profile)

    return render(request, 'church/update-profile.html', {'form': form, 'user': profile})



@login_required
def createDonation(request):
    form = DonationForm()

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form }
    return render(request, "church/donation-form.html", context)

@login_required
def upcoming_birthdays(request):
    today = datetime.today()
    upcoming_birthdays = CustomUser.objects.filter(
        birth_date__month=today.month,
        birth_date__day__gte=today.day
    ).order_by('birth_date__day')

    context = {'upcoming_birthdays': upcoming_birthdays}
    return render(request, 'church/upcoming-birthdays.html', context)




