# Generated by Django 4.1.7 on 2023-03-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_head_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='blog/img/%Y/%m/%d'),
        ),
    ]
