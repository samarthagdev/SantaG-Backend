# Generated by Django 3.1.3 on 2020-12-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfferPoster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='media/offerposter/')),
                ('url', models.CharField(max_length=40)),
            ],
        ),
    ]
