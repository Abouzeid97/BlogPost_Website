# Generated by Django 5.0 on 2024-01-13 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0003_tag_book_slug_remove_book_tag_book_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Post',
        ),
    ]