# Generated by Django 4.0.2 on 2022-03-23 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_alter_articles_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='for_moderation',
            field=models.BooleanField(default=True, verbose_name='На модерации'),
        ),
    ]
