# Generated by Django 3.2.8 on 2021-12-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sach',
            name='book_tacgia',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
