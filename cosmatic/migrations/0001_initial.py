# Generated by Django 3.1.3 on 2020-11-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cosmaticitems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cosBrand', models.CharField(max_length=70)),
                ('cosName', models.CharField(max_length=70)),
                ('cosPrice', models.IntegerField()),
                ('cosDis', models.FloatField(blank=True, max_length=30, null=True)),
                ('cosQuantity', models.IntegerField()),
                ('cosImage1', models.ImageField(blank=True, upload_to='media/cosmaticimages/')),
                ('cosImage2', models.ImageField(blank=True, upload_to='media/cosmaticimages/')),
                ('cosImage3', models.ImageField(blank=True, upload_to='media/cosmaticimages/')),
                ('cosImage4', models.ImageField(blank=True, upload_to='media/cosmaticimages/')),
                ('cosToken', models.CharField(blank=True, max_length=70)),
            ],
        ),
    ]
