# Generated by Django 3.1.3 on 2021-11-03 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restro', '0008_previousstoredata_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previousstoredata',
            name='position',
            field=models.CharField(default='finalize', max_length=70),
        ),
    ]
