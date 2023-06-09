# Generated by Django 4.1.7 on 2023-04-04 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_author_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Author',
            new_name='author',
        ),
    ]
