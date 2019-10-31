from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Picture, PictureShaderSettings


class PictureAdmin(admin.ModelAdmin):
    list_display = ["__str__", "preview_url"]

    def preview_url(self, obj):
        return mark_safe("<a href=\"{}\" target=\"_blank\">preview url</a>".format(obj.get_preview_url))


admin.site.register(Picture, PictureAdmin)


class PictureShaderSettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(PictureShaderSettings, PictureShaderSettingsAdmin)
