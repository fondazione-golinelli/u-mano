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


class ArtworkCard(models.Model):
    artwork = models.ForeignKey(Artwork, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=False, null=False)
    author = models.CharField(max_length=64, blank=False, null=False)
    abstract = models.CharField(max_length=2048, default="", blank=True, null=True)
    body = models.CharField(max_length=4096, default="", blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.artwork, self.title)

    def to_rich_text(self):
        return self.body


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


class ArtworkGraphNode(models.Model):
    artwork = models.ForeignKey(Artwork, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=False, null=False)
    kind = models.IntegerField(default=5, blank=False, null=False, choices=(
        (0, "ARTWORK CARD"),
        (1, "WEB QUERY"),
        (2, "IMAGES GALLERY")
    ))
    position = models.IntegerField(default=0, blank=False, null=False,
                                   help_text="Interactive node position in graph (zero based)")

    def __str__(self):
        return "{} - #{} {}  position {}".format(self.artwork, self.kind, self.title, self.position)


class ArtworkGraphSettings(models.Model):
    artwork = models.ForeignKey(Artwork, null=True, on_delete=models.CASCADE)
    x_dim = models.IntegerField(default=5, blank=False, null=False)
    y_dim = models.IntegerField(default=5, blank=False, null=False)
    z_dim = models.IntegerField(default=3, blank=False, null=False)
    max_lines = models.IntegerField(default=2, blank=False, null=False)
    density = models.IntegerField(default=7, blank=False, null=False)
    seed = models.IntegerField(default=9, blank=False, null=False)
    random_seed = models.BooleanField(default=False)
    min_distance = models.FloatField(default=3.0, blank=False, null=False)
    duration = models.FloatField(default=1.0, blank=False, null=False)
    y_mov = models.FloatField(default=0.05, blank=False, null=False)
    x_mov = models.FloatField(default=0.05, blank=False, null=False)
    z_mov = models.FloatField(default=0.05, blank=False, null=False)

    def __str__(self):
        return "{} graph settings".format(self.artwork)


class ArtworkQueryResultWebsite(models.Model):
    domain = models.CharField(max_length=64, blank=False, null=False, default="example.org")
    favicon = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "#{} {}".format(self.pk, self.domain)


class ArtworkQueryResult(models.Model):
    url = models.URLField(blank=False, null=False, max_length=512)
    website = models.ForeignKey(ArtworkQueryResultWebsite, null=True, on_delete=models.CASCADE)
    weight = models.FloatField(blank=False, null=False, default=0.0)
    artwork = models.ForeignKey(Artwork, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class ArtworkQueryTextResult(ArtworkQueryResult):
    title = models.CharField(max_length=512, default="", blank=True, null=True)
    body = models.CharField(max_length=2048, default="", blank=True, null=True)

    def __str__(self):
        return "{} - {} {}".format(self.artwork.title, self.website.domain, self.title)

    def to_rich_text(self):
        return self.body


class ArtworkQueryImageResult(ArtworkQueryResult):
    image = models.ImageField(blank=False, null=False)

    def __str__(self):
        return "{} - {} {}".format(self.artwork.title, self.website.domain, self.image.name)
