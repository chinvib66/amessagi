from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from .forms import MessageForm
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf
# Create your views here.
#@csrf_protect
def index(request):
    template = 'index.html'
    try:
        del request.session['amuser']
    except KeyError:
        pass
    if request.user.is_authenticated:
        context = {
            'msg': "Please Sign Out to send messages using a_Messagi.",
            
        }
        return render_to_response(template, context)
    else:
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/index/')
        else:
            context = {}
            context['form'] = MessageForm()
            context.update(csrf(request))
            return render_to_response(template, context)