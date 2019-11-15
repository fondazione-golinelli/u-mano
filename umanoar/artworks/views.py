import os
import json

from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArtworkSerializer, ArtworkLightSerializer, Artwork


class ArtworkList(APIView):
    def get(self, request, format=None):
        tree = request.GET.get("tree", False)

        artworks = Artwork.objects.all()
        serializer = ArtworkSerializer(artworks, many=True, context={"request": request, "tree": tree})
        return Response(serializer.data)


@csrf_exempt
def post_like(request, uid):
    if request.method == "POST":
        artwork = Artwork.objects.get(uid=uid)
        artwork.likes += 1
        artwork.save()
        serializer = ArtworkLightSerializer(artwork)
        return JsonResponse(serializer.data)
    return HttpResponseBadRequest()


@csrf_exempt
def post_visit(request, uid):
    if request.method == "POST":
        artwork = Artwork.objects.get(uid=uid)
        artwork.visits += 1
        artwork.save()
        serializer = ArtworkLightSerializer(artwork)
        return JsonResponse(serializer.data)
    return HttpResponseBadRequest()


@csrf_exempt
def post_interaction(request, uid):
    if request.method == "POST":
        artwork = Artwork.objects.get(uid=uid)
        artwork.interactions += 1
        artwork.save()
        serializer = ArtworkLightSerializer(artwork)
        return JsonResponse(serializer.data)
    return HttpResponseBadRequest()


@csrf_exempt
def post_time(request, uid):
    if request.method == "POST":
        if request.content_type == "application/json":
            tt = float(json.loads(request.body).get("time"))
        else:
            tt = float(request.POST.get("time"))
        artwork = Artwork.objects.get(uid=uid)
        if tt > artwork.max_time:
            artwork.max_time = tt
        if tt < artwork.min_time or artwork.min_time == 0.0:
            artwork.min_time = tt
        artwork.avg_time += tt / max([artwork.visits, 1])
        artwork.save()
        serializer = ArtworkLightSerializer(artwork)
        return JsonResponse(serializer.data)
    return HttpResponseBadRequest()



@csrf_exempt
def count_missing_contents(request):
    if request.method == "POST":
        total_size = 0
        if request.content_type == "application/json":
            for c in json.loads(request.body).get("contents"):
                total_size += os.path.getsize(os.path.join(settings.MEDIA_ROOT, c))
            return JsonResponse(dict(size=total_size))

    return HttpResponseBadRequest()
