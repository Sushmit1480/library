# Generated by Django 3.1 on 2020-09-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20200920_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='total_copies',
            field=models.IntegerField(default=0),
        ),
    ]
