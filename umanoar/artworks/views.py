

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArtworkSerializer, Artwork


class ArtworkList(APIView):
    def get(self, request, format=None):
        artworks = Artwork.objects.all()
        serializer = ArtworkSerializer(artworks, many=True)
        return Response(serializer.data)



# TODO
# GET statistics
# POST like
# POST metric
# POST image?!