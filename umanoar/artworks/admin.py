from django.contrib import admin
from .models import Artwork, ShaderParameters, ApplicationSettings, ArtworkQueryResultWebsite, \
    ArtworkQueryTextResult, ArtworkQueryImageResult


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
