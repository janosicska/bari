# Generated by Django 3.0.6 on 2020-12-01 22:04

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Classified Address')),
                ('photo', models.ImageField(blank=True, upload_to='classifieds/%Y/%m/%d/')),
                ('category', models.CharField(choices=[(None, 'Select the category'), ('RealEstate', 'Real Estate'), ('Cars', 'Cars'), ('Clothing', 'Clothing'), ('Furniture', 'Furniture'), ('Technology', 'Technology'), ('Services', 'Services')], max_length=20, null=True)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
