# Generated by Django 2.2.1 on 2019-05-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cau_quiz', '0003_auto_20190524_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='medal',
            field=models.CharField(default='hi', max_length=10),
        ),
    ]
