from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'pages/users/list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone']
        )
        return redirect('user_list')
    return render(request, 'pages/users/form.html')