from django.shortcuts import redirect
from .models import Shopuser

def login_required(function):
    def wrap(request, *args, **kwargs):
        shopuser = request.session.get('user')
        if shopuser is None or not shopuser:
            return redirect('/login')
        return function(request, *args, **kwargs)
    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        shopuser = request.session.get('user')
        if shopuser is None or not shopuser:
            return redirect('/login')
        
        shopuser = Shopuser.objects.get(email = shopuser)
        if shopuser.level != 'admin':
            return redirect('/')
        return function(request, *args, **kwargs)
    return wrap