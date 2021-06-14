# Generated by Django 3.2.4 on 2021-06-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations_event', '0006_alter_tags_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='locations_event.Tags', verbose_name='Тэги'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Тэг'),
        ),
    ]
