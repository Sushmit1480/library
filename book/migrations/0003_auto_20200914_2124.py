# Generated by Django 3.1 on 2020-09-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200914_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], max_length=3),
        ),
    ]