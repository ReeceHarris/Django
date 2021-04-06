# Generated by Django 3.1.7 on 2021-04-01 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20210331_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('', ''), ('Mrs.', 'Mrs.')], default='', max_length=6),
        ),
    ]
