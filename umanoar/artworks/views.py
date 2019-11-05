from django.http import JsonResponse, HttpResponseBadRequest

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArtworkSerializer, ArtworkLightSerializer, Artwork
from django.views.decorators.csrf import csrf_exempt


class ArtworkList(APIView):
    def get(self, request, format=None):
        artworks = Artwork.objects.all()
        serializer = ArtworkSerializer(artworks, many=True, context={"request": request})
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
