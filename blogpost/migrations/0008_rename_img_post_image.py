# Generated by Django 5.0 on 2024-01-27 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0007_post_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='img',
            new_name='image',
        ),
    ]
