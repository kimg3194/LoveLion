# Generated by Django 2.2.1 on 2019-05-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cau_quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
