# Generated by Django 4.0.5 on 2022-06-27 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_slug_alter_blog_slug_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]