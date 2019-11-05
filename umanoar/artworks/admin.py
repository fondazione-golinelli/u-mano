from django.contrib import admin
from .models import Artwork, ShaderParameters, ApplicationSettings, ArtworkQueryResultWebsite, \
    ArtworkQueryTextResult, ArtworkQueryImageResult, ArtworkGraphNode, ArtworkCard, ArtworkGraphSettings


class ArtworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artwork, ArtworkAdmin)


class ShaderParametersAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShaderParameters, ShaderParametersAdmin)


class ApplicationSettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ApplicationSettings, ApplicationSettingsAdmin)


class ArtworkQueryResultWebsiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArtworkQueryResultWebsite, ArtworkQueryResultWebsiteAdmin)


class ArtworkQueryTextResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArtworkQueryTextResult, ArtworkQueryTextResultAdmin)


class ArtworkQueryImageResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArtworkQueryImageResult, ArtworkQueryImageResultAdmin)


class ArtworkGraphNodeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArtworkGraphNode, ArtworkGraphNodeAdmin)


class ArtworkCardAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArtworkCard, ArtworkCardAdmin)


class ArtworkGraphSettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArtworkGraphSettings, ArtworkGraphSettingsAdmin)
