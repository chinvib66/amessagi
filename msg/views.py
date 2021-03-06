from django.shortcuts import render, render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import MessageForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf
from users.models import a_M_user
# Create your views here.
#@csrf_protect
def index(request):
    template = 'index.html'
    context = {}
    try:
        del request.session['amuser']
    except KeyError:
        pass
    if request.user.is_authenticated:
        context['amuser'] = get_object_or_404(a_M_user, user = request.user)
        context['st']= "Please Sign Out to send messages using a_Messagi."
        request.session
        return render_to_response(template, context)
    else:
        if request.method == 'POST':
            form = MessageForm(request.POST)
            try:
                amuser =  a_M_user.objects.get(am_add = request.POST['rec_add'])
                if amuser:
                    form.save()
                    context['msg']= "Message Sent"
            except:
                    context['msg']= "Invalid Address. Please Enter correct address."
        else:
            pass
        context['form'] = MessageForm()
        context.update(csrf(request)) 
        return render_to_response(template, context)