# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0005_auto_20180326_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]