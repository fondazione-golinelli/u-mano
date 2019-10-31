import mimetypes
from django.db import models
from django.core import validators


class Artwork(models.Model):
    class Meta:
        verbose_name = "AR artwork"
        verbose_name_plural = "AR artworks"
    uid = models.CharField(max_length=36, blank=False, null=False)
    title = models.CharField(max_length=64, blank=False, null=False)
    shader = models.ForeignKey("ShaderParameters", on_delete=models.SET_NULL, null=True, blank=True)

    stats = models.ForeignKey("ArtworkStatistics", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.uid, self.title)


class ArtworkInformation(models.Model):
    class Meta:
        verbose_name = "AR artwork information"
        verbose_name_plural = "AR artwork informations"
    title = models.CharField(max_length=64, blank=False, null=False)
    mime = models.CharField(max_length=32, default="txt/plain", blank=False, null=False)
    summary = models.CharField(max_length=128, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    weight = models.FloatField(default=0, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(1)])
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    url = models.URLField(max_length=256, blank=True, null=True)
    interactive = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.mime, self.artwork)


class ShaderParameters(models.Model):
    class Meta:
        verbose_name = "AR shader parameters"
        verbose_name_plural = "AR shader parameters"

    parameters = models.CharField(max_length=512, blank=False, null=False,
                                  validators=[validators.validate_comma_separated_integer_list])


class ApplicationSettings(models.Model):
    class Meta:
        verbose_name = "AR application settings"
        verbose_name_plural = "AR shader settings"

    chaos = models.FloatField(default=0, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(1)])


class ArtworkStatistics(models.Model):
    interactions = models.IntegerField(default=0, blank=False, null=False)
    visits = models.IntegerField(default=0, blank=False, null=False)
    likes = models.IntegerField(default=0, blank=False, null=False)
    avg_time = models.FloatField(default=0, blank=False, null=False)
    max_time = models.FloatField(default=0, blank=False, null=False)
    min_time = models.FloatField(default=0, blank=False, null=False)
    hashtags = models.CharField(max_length=512, default="", blank=True, null=True)
