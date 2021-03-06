# Generated by Django 3.1 on 2020-09-20 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_auto_20200919_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='copies',
        ),
        migrations.AddField(
            model_name='book',
            name='remaining',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='total_copies',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='book_assign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
    ]
