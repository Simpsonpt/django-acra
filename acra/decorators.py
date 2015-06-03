from django.http import HttpResponse
from functools import wraps

def http_basic_auth(func):
    @wraps(func)
    def _decorator(request, *args, **kwargs):
        from django.contrib.auth import authenticate, login
        if request.META.has_key('HTTP_AUTHORIZATION'):
            authmeth, auth = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
            if authmeth.lower() == 'basic':
                auth = auth.strip().decode('base64')
                username, password = auth.split(':', 1)
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.has_perm('acra.add_crashreport') and user.has_perm('acra.change_crashreport') and user.has_perm('acra.delete_crashreport'):
                        login(request, user)
                        return func(request, *args, **kwargs)
        response = HttpResponse()
        response.status_code = 401
        return response
    return _decorator
