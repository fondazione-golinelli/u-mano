from rest_framework import serializers

from .models import Artwork, ArtworkInformation, ApplicationSettings, ShaderParameters


class ArtworkInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkInformation
        exclude = ['id', 'artwork']


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
        exclude = ['id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        infos = ArtworkInformation.objects.filter(artwork=instance).all()
        data['nodes'] = ArtworkInformationSerializer(infos, many=True).data

        data['shader'] = None
        if instance.shader is not None:
            data['shader'] = dict(parameters=map(float, instance.shader.parameters.split(",")))

        data['settings'] = ApplicationSettingsSerializer(ApplicationSettings.objects.first()).data

        return data
