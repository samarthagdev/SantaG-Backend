# Generated by Django 3.1.3 on 2021-11-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restro', '0007_auto_20210927_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='previousstoredata',
            name='position',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
