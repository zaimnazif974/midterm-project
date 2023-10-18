from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse



# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            #Setting default role
            default_group = Group.objects.get(name='member')
            user.groups.add(default_group)
            print(default_group)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'LOGIN SUCCESFUL') # sementara
            print(user.groups.all()[0])

            #Nentuin member atau admin
            if(user.groups.all()[0].name == 'admin'):
                return HttpResponseRedirect(reverse('admin_page:show_main'))
            elif(user.groups.all()[0].name == 'member'):
                # return HttpResponseRedirect(reverse('admin_page:show_main')) ini buat ke landing page
                print('halo')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)