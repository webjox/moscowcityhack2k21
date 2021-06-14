# Generated by Django 3.2.4 on 2021-06-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID места')),
                ('title', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('place_type_id', models.IntegerField(blank=True, null=True)),
                ('foundation_id', models.IntegerField(blank=True, null=True)),
                ('ebs_id', models.IntegerField(blank=True, null=True)),
                ('ebs_title', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]