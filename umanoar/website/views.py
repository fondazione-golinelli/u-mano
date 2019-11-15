from django.shortcuts import render, render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response(
        'website/index.html', {},
        RequestContext(request)
    )


def privacy_policy(request):
    return render_to_response(
        'website/privacy_policy.html'
    )

