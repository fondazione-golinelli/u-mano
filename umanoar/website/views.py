from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

import user_agents


def home(request):
    useragent = user_agents.parse(request.META.get("HTTP_USER_AGENT"))
    if useragent.os.family == "Android":
        return HttpResponseRedirect(settings.PLAY_STORE_URL)
    elif useragent.os.family == "iOS" or "Mac OS" in useragent.os.family:
        return HttpResponseRedirect(settings.APP_STORE_URL)
    return render_to_response(
        'website/index.html', {},
        RequestContext(request)
    )


def privacy_policy(request):
    return render_to_response(
        'website/privacy_policy.html'
    )
