# Generated by Django 5.1.4 on 2024-12-27 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookman', '0004_alter_book_isbn_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_number',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]