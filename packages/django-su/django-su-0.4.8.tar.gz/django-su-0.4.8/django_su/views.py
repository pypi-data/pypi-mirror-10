# -*- coding: utf-8 -*-

import warnings

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_http_methods
from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

try:
    from django.contrib.auth import get_user_model

    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

from .forms import UserSuForm
from .utils import su_login_callback, custom_login_action


@require_http_methods(['POST'])
@user_passes_test(su_login_callback)
def login_as_user(request, user_id):
    userobj = authenticate(su=True, pk=user_id)
    if not userobj:
        raise Http404("User not found")

    exit_users_pk = request.session.get("exit_users_pk", default=[])
    exit_users_pk.append(
        (request.session[SESSION_KEY], request.session[BACKEND_SESSION_KEY]))

    if not custom_login_action(request, userobj):
        login(request, userobj)
    request.session["exit_users_pk"] = exit_users_pk

    if hasattr(settings, 'SU_REDIRECT_LOGIN'):
        warnings.warn("SU_REDIRECT_LOGIN is deprecated, use SU_LOGIN_REDIRECT_URL", DeprecationWarning)

    return HttpResponseRedirect(
        getattr(settings, "SU_LOGIN_REDIRECT_URL", "/"))


@require_http_methods(['POST', 'GET'])
@user_passes_test(su_login_callback)
def su_login(request, form_class=UserSuForm, template_name='su/login.html'):
    form = form_class(request.POST or None)
    if form.is_valid():
        return login_as_user(request, form.get_user().pk)
    
    return render_to_response(template_name,{
        'form': form,
    }, context_instance=RequestContext(request))


def su_logout(request):
    exit_users_pk = request.session.get("exit_users_pk", default=[])
    if not exit_users_pk:
        return HttpResponseBadRequest(
            ("This session was not su'ed into. Cannot exit."))

    user_id, backend = exit_users_pk.pop()

    userobj = get_object_or_404(User, pk=user_id)
    userobj.backend = backend

    if not custom_login_action(request, userobj):
        login(request, userobj)
    request.session["exit_users_pk"] = exit_users_pk

    if hasattr(settings, 'SU_REDIRECT_EXIT'):
        warnings.warn("SU_REDIRECT_EXIT is deprecated, use SU_LOGOUT_REDIRECT_URL", DeprecationWarning)

    return HttpResponseRedirect(
        getattr(settings, "SU_LOGOUT_REDIRECT_URL", "/"))
