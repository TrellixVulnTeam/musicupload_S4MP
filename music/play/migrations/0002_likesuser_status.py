# Generated by Django 3.0.1 on 2020-08-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likesuser',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
