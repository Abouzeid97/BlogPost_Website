# Generated by Django 5.0 on 2024-03-14 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0011_alter_post_time_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=120)),
                ('user_email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=600)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogpost.post')),
            ],
        ),
    ]
