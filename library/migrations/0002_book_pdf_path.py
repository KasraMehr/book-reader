# Generated by Django 5.0.6 on 2024-07-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf_path',
            field=models.FilePathField(default='books/mml-book.pdf', path='books/'),
        ),
    ]