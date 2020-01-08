"""umanoar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from artworks import views as artwork_views
from demo import views as demo_views
from website import views as website_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/artworks/', artwork_views.ArtworkList.as_view()),
    path('api/artworks/<str:uid>/like', artwork_views.post_like),
    path('api/artworks/<str:uid>/like/', artwork_views.post_like),
    path('api/artworks/<str:uid>/visit', artwork_views.post_visit),
    path('api/artworks/<str:uid>/visit/', artwork_views.post_visit),
    path('api/artworks/<str:uid>/interaction', artwork_views.post_interaction),
    path('api/artworks/<str:uid>/interaction/', artwork_views.post_interaction),
    path('api/artworks/<str:uid>/time', artwork_views.post_time),
    path('api/artworks/<str:uid>/time/', artwork_views.post_time),
    path('api/artworks/missing/', artwork_views.count_missing_contents),
    path('api/artworks/live/', artwork_views.live),

    path('demo/picture/<int:pk>', demo_views.picture_preview, name="umano_demo_picture_preview"),
    path('demo/updateshader/', demo_views.update_shader_settings, name="umano_demo_update_shader"),
    # path('', demo_views.demo_one)
    path('privacy-policy', website_views.privacy_policy, name="privacy_policy"),
    path('', website_views.home)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
