# Generated by Django 4.2.7 on 2024-05-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
