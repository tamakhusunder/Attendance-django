# Generated by Django 3.0.3 on 2021-02-23 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherdb',
            name='image',
            field=models.ImageField(upload_to='faceapp/images/staffs'),
        ),
    ]
