# Generated by Django 2.2.5 on 2019-10-03 14:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='shader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='demo.PictureShaderSettings', verbose_name='Shader Settings'),
        ),
        migrations.AlterField(
            model_name='pictureshadersettings',
            name='particle_depth',
            field=models.FloatField(default=4.0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='pictureshadersettings',
            name='particle_random',
            field=models.FloatField(default=2.0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='pictureshadersettings',
            name='particle_size',
            field=models.FloatField(default=1.5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='pictureshadersettings',
            name='touch_radius',
            field=models.FloatField(default=0.15, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0.5)]),
        ),
    ]
