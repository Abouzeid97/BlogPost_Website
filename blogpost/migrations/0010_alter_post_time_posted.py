# Generated by Django 5.0 on 2024-01-31 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0009_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_posted',
            field=models.DateField(blank=True),
        ),
    ]