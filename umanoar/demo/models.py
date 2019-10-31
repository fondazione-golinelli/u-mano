from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Picture(models.Model):
    image = models.ImageField(blank=False, null=False, help_text="Maximum recommended size: 800x600")
    description = models.CharField(max_length=256, blank=True, null=True)
    shader = models.ForeignKey("PictureShaderSettings", verbose_name="Shader Settings", blank=True, null=True,
                               on_delete=models.SET_NULL)

    @property
    def get_preview_url(self):
        return reverse('umano_demo_picture_preview', args=(self.id,))

    def __str__(self):
        return "Picture #{} {}".format(self.id, self.image)


class PictureShaderSettings(models.Model):
    touch_radius = models.FloatField(default=0.15, validators=[MinValueValidator(0), MaxValueValidator(0.5)])
    particle_random = models.FloatField(default=2.0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    particle_depth = models.FloatField(default=4.0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    particle_size = models.FloatField(default=1.5, validators=[MinValueValidator(0), MaxValueValidator(3)])

    def __str__(self):
        return "Shader settings (radius: {}, random: {}, depth: {}, size: {})".format(
            self.touch_radius, self.particle_random, self.particle_depth, self.particle_size
        )
