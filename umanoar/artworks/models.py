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

    query_keyword = models.CharField(max_length=128, blank=True, null=True)

    interactions = models.IntegerField(default=0, blank=False, null=False)

    visits = models.IntegerField(default=0.0, blank=False, null=False)
    likes = models.IntegerField(default=0.0, blank=False, null=False)
    avg_time = models.FloatField(default=0.0, blank=False, null=False)
    max_time = models.FloatField(default=0.0, blank=False, null=False)
    min_time = models.FloatField(default=0.0, blank=False, null=False)
    score = models.FloatField(default=0.0, blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.uid, self.title)

    def get_query(self):
        return self.query_keyword or self.title


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


class ArtworkQueryResultWebsite(models.Model):
    domain = models.CharField(max_length=64, blank=False, null=False, default="example.org")
    favicon = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "#{} {}".format(self.pk, self.domain)


class ArtworkQueryResult(models.Model):
    url = models.URLField(blank=False, null=False)
    website = models.ForeignKey(ArtworkQueryResultWebsite, null=True, on_delete=models.CASCADE)
    weight = models.FloatField(blank=False, null=False, default=0.0)
    artwork = models.ForeignKey(Artwork, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class ArtworkQueryTextResult(ArtworkQueryResult):
    title = models.CharField(max_length=512, default="", blank=True, null=True)
    abstract = models.CharField(max_length=1024, default="", blank=True, null=True)

    def __str__(self):
        return "{} - {} {}".format(self.artwork.title, self.website.domain, self.title)


class ArtworkQueryImageResult(ArtworkQueryResult):
    image = models.ImageField(blank=False, null=False)

    def __str__(self):
        return "{} - {} {}".format(self.artwork.title, self.website.domain, self.image.name)
