# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import produits.models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0003_produit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=produits.models.upload_image_path),
        ),
    ]