# Generated by Django 3.2.13 on 2022-06-13 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodgram', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='color_hexcode',
            new_name='color',
        ),
    ]
