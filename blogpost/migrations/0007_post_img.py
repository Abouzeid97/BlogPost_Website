# Generated by Django 5.0 on 2024-01-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0006_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='', upload_to='post/'),
        ),
    ]
