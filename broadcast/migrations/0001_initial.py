# Generated by Django 3.1.3 on 2020-11-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otpveification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
                ('number', models.CharField(blank=True, max_length=30, null=True)),
                ('otp', models.IntegerField(blank=True, default=0)),
                ('number_trial', models.IntegerField(blank=True, default=0)),
                ('timestamps', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
