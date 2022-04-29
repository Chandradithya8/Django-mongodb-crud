from django.shortcuts import render, redirect
from .models import User
from .form import Add_A_User

def home(request):
    users = User.objects.all() 
    context = {'users': users}
    return render(request, 'home.html', context)

def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        phone_number = request.POST['pno']
        form = User(name = name, email = email, gender = gender, phone_number = phone_number)
        form.save()
        return redirect('/')


    return render(request, 'add.html')


def update(request, id):
    users = User.objects.filter(id=id).first()
    context = {'users': users}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        phone_number = request.POST['pno']

        form = User(id=id, name=name, email=email, gender=gender, phone_number=phone_number)
        form.save()
        return redirect('/')
    
    return render(request, 'update.html', context)

def delete(request, id):
    delete_user = User.objects.filter(id=id)
    delete_user.delete()
    return redirect('/')
