# Generated by Django 3.1.7 on 2021-03-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20210329_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(blank=True, choices=[('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('', ''), ('Mr.', 'Mr.')], default='', max_length=6),
        ),
    ]
