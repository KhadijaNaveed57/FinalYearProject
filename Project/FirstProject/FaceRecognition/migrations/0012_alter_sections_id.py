# Generated by Django 3.2.1 on 2021-06-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0011_alter_sections_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
