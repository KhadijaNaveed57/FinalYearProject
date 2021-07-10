# Generated by Django 3.2.1 on 2021-05-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0002_rename_signup_admindata'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('fathername', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=70)),
                ('gender', models.BinaryField()),
                ('department', models.CharField(max_length=50)),
                ('subjects', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('id', models.CharField(max_length=50, primary_key=1, serialize=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
