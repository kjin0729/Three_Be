# Generated by Django 3.2 on 2021-05-20 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='サムネイル'),
        ),
    ]