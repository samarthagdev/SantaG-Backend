# Generated by Django 3.1.3 on 2021-07-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firbase', '0002_auto_20210720_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetoken',
            name='fcm_token',
            field=models.CharField(max_length=400),
        ),
    ]
