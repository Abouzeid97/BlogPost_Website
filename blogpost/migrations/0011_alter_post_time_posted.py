# Generated by Django 5.0 on 2024-01-31 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0010_alter_post_time_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_posted',
            field=models.DateField(),
        ),
    ]
