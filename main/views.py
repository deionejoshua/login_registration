from django.shortcuts import render, redirect
import bcrypt
from .models import user_info
from django.contrib import messages



def index(request):
    return render(request, 'index.html')


def register(request):
    errors = user_info.objects.validation(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg )
        return redirect('/')

    hashed_pw = bcrypt.hashpw(request.POST['user_password'].encode(), bcrypt.gensalt()).decode()
    
    created_user = user_info.objects.create (
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        password = hashed_pw,

    )
    request.session['user_id'] = created_user.id
    return redirect('/user_login')


def dashboard(request):
    context = {
        "user": user_info.objects.get(id=request.session['user_id'])
    }
    return render(request, 'dashboard.html', context)




def process_login(request):
    user_list = user_info.objects.filter(email_address = request.POST['email_address'])
    if len(user_list) != 0:
        user = user_list[0]

        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/dashboard')

    messages.error(request, "Email and/or password incorrect")
    return redirect('/user_login')


def login_page(request):
    return render(request, 'login.html')



def logout(request):
    request.session.flush()
    return redirect('/')