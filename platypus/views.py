import socket

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

socket.setdefaulttimeout(7)

def template(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

def temp_sync(request):
    from platypus.apps.xbox.models import sync_xbox
    sync_xbox()

def login(request):
    redirect_to = request.GET.get('next', '/')
    
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    
    form = forms.LoginForm(request.POST or None)
    
    if form.is_valid():
        user = auth.authenticate(username = form.cleaned_data['username'],
                                 password = form.cleaned_data['password'])
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(redirect_to)

    return render_to_response('login.html', {
        'title': 'login',
        'form': form,
        'next': request.GET.get('next', '')
    }, context_instance = RequestContext(request))

def logout(request):
    return auth_views.logout(request, next_page=request.GET.get('next', '/'))

def home(request):
    return template(request, 'base.html')