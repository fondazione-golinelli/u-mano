import os
import networkx as nx
from rest_framework import serializers

from .models import Artwork, ApplicationSettings, ShaderParameters, ArtworkQueryTextResult, \
    ArtworkQueryImageResult, ArtworkQueryResultWebsite, ArtworkGraphSettings, ArtworkGraphNode, ArtworkCard


def to_query_node(instance, data, request):
    default = dict(
        id=0,
        children=[],
        url=None,
        website=None,
        favicon=None,
        title=None,
        body=None
    )

    data.update(default)

    if isinstance(instance, (ArtworkQueryTextResult, ArtworkCard)):
        data['title'] = instance.title
        data['body'] = instance.to_rich_text()

    if isinstance(instance, (ArtworkQueryTextResult, ArtworkQueryImageResult)):
        data['website'] = instance.website.domain
        # try:
        #     if instance.website.favicon:
        #         if instance.website.favicon.path.endswith(".png") or os.path.exists(instance.website.favicon.path.replace(".ico", ".png")):
        #             data['favicon'] = "{}://{}/media/{}".format(request.scheme, request.META.get("HTTP_HOST"),
        #                                                         instance.website.favicon.name.replace(".ico", ".png"))
        #         else:
        #             data['favicon'] = None
        # except:
        data['favicon'] = "{}://{}/static/images/default_favicon.png".format(request.scheme, request.META.get("HTTP_HOST"))
        data['url'] = instance.url

    if isinstance(instance, ArtworkQueryImageResult):
        data['url'] = "{}://{}{}".format(request.scheme, request.META.get("HTTP_HOST"), data['image'])
        data['title'] = "Scaricata da {}".format(instance.website.domain)
        data.pop("image")

    return data


class ArtworkQueryResultWebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkQueryResultWebsite
        exclude = ['id']


class ArtworkGraphSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkGraphSettings
        exclude = ['id', 'artwork']


class ArtworkGraphNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkGraphNode
        exclude = ['id', 'artwork']


class ArtworkCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkCard
        exclude = ['id', 'artwork', 'abstract', 'author', 'author_info', 'date']


class ArtworkQueryTextResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkQueryTextResult
        exclude = ['id', 'artwork', 'weight']


class ArtworkQueryImageResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkQueryImageResult
        exclude = ['id', 'artwork', 'weight']


class ApplicationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationSettings
        fields = ['chaos']


class ShaderParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShaderParameters
        fields = ["parameters"]


class ArtworkLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        exclude = ['id', 'query_keyword', 'shader']



class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        exclude = ['id', 'query_keyword', 'shader']

    def to_representation(self, instance):
        request = self.context.get('request', None)
        tree = self.context.get("tree")

        data = super().to_representation(instance)

        # data['shader'] = None
        # if instance.shader is not None:
        #     data['shader'] = dict(parameters=map(float, instance.shader.parameters.split(",")))

        data['settings'] = ArtworkGraphSettingsSerializer(
            ArtworkGraphSettings.objects.filter(artwork=instance).first()).data

        data['nodes'] = []
        for node in ArtworkGraphNode.objects.filter(artwork=instance).all():
            data_node = ArtworkGraphNodeSerializer(node).data
            data_node['query'] = []
            if node.kind == 0:
                card = ArtworkCard.objects.filter(artwork=instance).first()
                if card is not None:
                    data_node['query'].append(
                        to_query_node(card, ArtworkCardSerializer(card).data, request)
                    )
            elif node.kind == 1:
                query_results = [
                    (i, x) for i, x in enumerate(ArtworkQueryTextResult.objects.filter(artwork=instance).all())
                ]
                G = nx.random_internet_as_graph(len(query_results), seed=42)
                if tree:
                    print("tree!")
                    G = nx.algorithms.minimum_spanning_tree(G)
                ad_list = dict([(i, x) for i, x in enumerate(nx.adjlist.generate_adjlist(G))])

                for i, q in query_results:
                    q_data = ArtworkQueryTextResultSerializer(q).data
                    q_data = to_query_node(q, q_data, request)
                    q_data['id'] = i
                    children = list(map(int, ad_list[i].split()))
                    if i in children:
                        children.remove(i)
                    q_data['children'] = children
                    data_node['query'].append(q_data)

            else:  # if node.kind == 2:
                for image in ArtworkQueryImageResult.objects.filter(artwork=instance).all():
                    data_node['query'].append(
                        to_query_node(image, ArtworkQueryImageResultSerializer(image).data, request)
                    )

            data_node['title'] = node.get_title()
            data['nodes'].append(
                data_node
            )

        return data
