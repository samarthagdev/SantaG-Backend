# Generated by Django 3.1.3 on 2021-02-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0004_auto_20210205_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bagadding',
            name='cosQuantity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
