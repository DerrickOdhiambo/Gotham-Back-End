# Generated by Django 3.1.3 on 2020-11-05 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(null=True, upload_to='posters'),
        ),
    ]
