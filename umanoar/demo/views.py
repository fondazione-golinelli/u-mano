from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from .models import PictureShaderSettings, Picture


# Create your views here.
def demo_one(request):
    return render_to_response(
        'demo/demo_one.html', {},
        RequestContext(request)
    )


def picture_preview(request, pk):
    pic = Picture.objects.get(pk=pk)

    if pic.shader is None:
        pic.shader = PictureShaderSettings()

    return render_to_response(
        'demo/demo_picture.html', {'picture': pic},
        RequestContext(request)
    )


@csrf_exempt
def update_shader_settings(request):
    if request.method == "POST":
        pic = Picture.objects.get(pk=request.POST.get("pk"))
        if pic.shader is None:
            pic.shader = PictureShaderSettings()
        pic.shader.particle_depth = request.POST.get("radius")
        pic.shader.particle_random = request.POST.get("random")
        pic.shader.particle_size = request.POST.get("size")
        pic.shader.touch_radius = request.POST.get("radius")
        pic.shader.save()
        pic.shader = PictureShaderSettings.objects.get(pk=pic.shader.pk)
        pic.save()

    return JsonResponse({'ok': True})
