# Generated by Django 2.2.5 on 2019-11-05 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0013_auto_20191105_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='artworkgraphsettings',
            name='artwork',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artworks.Artwork'),
        ),
    ]
