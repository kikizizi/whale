# Generated by Django 3.1.7 on 2022-04-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_head_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='blog/images/%Y/%m/%d/'),
        ),
    ]