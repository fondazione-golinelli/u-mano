import networkx as nx
from rest_framework import serializers

from .models import Artwork, ApplicationSettings, ShaderParameters, ArtworkQueryTextResult, \
    ArtworkQueryImageResult, ArtworkQueryResultWebsite


class ArtworkQueryResultWebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkQueryResultWebsite
        exclude = ['id']


class ArtworkQueryTextResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkQueryTextResult
        exclude = ['id', 'artwork', 'weight']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        website_data = ArtworkQueryResultWebsiteSerializer(instance.website).data
        data['website'] = instance.website.domain
        request = self.context.get('request', None)
        if request is not None and website_data['favicon'] is not None:
            data['favicon'] = "{}://{}{}".format(request.scheme, request.META.get("HTTP_HOST"), website_data['favicon'])
        else:
            data['favicon'] = None
        return data


class ArtworkQueryImageResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkQueryImageResult
        exclude = ['id', 'artwork', 'weight']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        website_data = ArtworkQueryResultWebsiteSerializer(instance.website).data
        data['website'] = instance.website.domain
        request = self.context.get('request', None)
        if request is not None and website_data['favicon'] is not None:
            data['favicon'] = "{}://{}{}".format(request.scheme, request.META.get("HTTP_HOST"), website_data['favicon'])
        else:
            data['favicon'] = None
        return data


class ApplicationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationSettings
        fields = ['chaos']


class ShaderParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShaderParameters
        fields = ["parameters"]


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        exclude = ['id', 'query_keyword']

    def to_representation(self, instance):
        request = self.context.get('request', None)

        data = super().to_representation(instance)

        data['shader'] = None
        if instance.shader is not None:
            data['shader'] = dict(parameters=map(float, instance.shader.parameters.split(",")))

        data['settings'] = ApplicationSettingsSerializer(ApplicationSettings.objects.first()).data

        data['query'] = []
        data['images'] = []

        query_results = [
            (i, x) for i, x in enumerate(ArtworkQueryTextResult.objects.all())
        ]
        G = nx.random_internet_as_graph(len(query_results), seed=42)
        adjlist = dict([(i, x) for i, x in enumerate(nx.adjlist.generate_adjlist(G))])

        for i, q in query_results:
            q_data = ArtworkQueryTextResultSerializer(q, context={"request": request}).data
            q_data['id'] = i
            children = list(map(int, adjlist[i].split()))
            if i in children:
                children.remove(i)
            q_data['children'] = children
            data['query'].append(q_data)
        data['images'] = ArtworkQueryImageResultSerializer(
            ArtworkQueryImageResult.objects.filter(artwork=instance).all(),
            many=True, context={"request": request}).data

        return data
