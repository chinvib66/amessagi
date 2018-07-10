from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from msg.models import Message
from .models import a_M_user
from django.template.context_processors import csrf
from .forms import UserRegForm, aMForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        
        if form.is_valid():
            user = form.cleaned_data
            amuser = a_M_user()
            first_name = user['first_name']
            last_name = user['first_name']
            username = user['username']
            password = user['password']
            email = user['email']
            if (User.objects.filter(username=username).exists()):
                raise forms.ValidationError('Looks like that username already exists')
            else:
                user = User.objects.create_user(username,email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                amuser.user = user
                amuser.am_add = username + '@amessagi.am'
                amuser.save()
                return HttpResponseRedirect('/user/login')
            
    else:
        context = {}
        context.update(csrf(request))
        context['form'] = UserRegForm()
        return render_to_response('register.html', context)
    #return HttpResponse('Hello, Currently inactive')

 
def dashboard(request):
    amuser = get_object_or_404(a_M_user, user = request.user)
    request.session['amuser']= amuser.id
    messages = Message.objects.filter(rec_add=amuser.am_add).all()
    context = {
        'messages': messages,
        'error': 'No Messages',
        'amuser': amuser,
    }
    return render_to_response('dashboard.html', context)

