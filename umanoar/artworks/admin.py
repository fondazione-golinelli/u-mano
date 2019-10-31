from django.contrib import admin
from .models import Artwork, ArtworkInformation, ShaderParameters, ApplicationSettings


class ArtworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artwork, ArtworkAdmin)


class ArtworkInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArtworkInformation, ArtworkInformationAdmin)


class ShaderParametersAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShaderParameters, ShaderParametersAdmin)


class ApplicationSettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ApplicationSettings, ApplicationSettingsAdmin)
