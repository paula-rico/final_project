from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import RegisterForm, UserUpdateForm, UserProfileForm
from users.models import UserProfile


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, 'index.html', {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,'index.html', {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, 'index.html', {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})




def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context ={
            'form':form
        }
        return render(request, 'users/register.html', context=context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            UserProfile.objects.create(user=user)
            return redirect('login')
            
        
        context = {
            'errors':form.errors,
            'form':RegisterForm()
        }
        return render(request, 'users/register.html', context=context)


@login_required
def update_user(request):
    user = request.user
    if request.method == 'GET':
        form = UserUpdateForm(initial = {
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,

        })
        context ={
            'form':form
        }
        return render(request, 'users/update_user.html', context=context)

    elif request.method == 'POST':
        form = UserUpdateForm(data=request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':RegisterForm()
        }
        return render(request, 'users/update_user.html', context=context)



def update_user_profile(request):
    user = request.user
    if request.method == 'GET':
        form = UserProfileForm(initial={
            'phone':request.user.profile.phone,
            'profession':request.user.profile.profession
        })
        context ={
            'form':form
        }
        return render(request, 'users/update_profile.html', context=context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.profession = form.cleaned_data.get('profession')
            user.profile.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':UserProfileForm()
        }
        return render(request, 'users/register.html', context=context)