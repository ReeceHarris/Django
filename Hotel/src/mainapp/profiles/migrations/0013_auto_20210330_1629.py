# Generated by Django 3.1.7 on 2021-03-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20210329_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(blank=True, choices=[('Mrs.', 'Mrs.'), ('', ''), ('Ms.', 'Ms.'), ('Mr.', 'Mr.')], default='', max_length=6),
        ),
    ]
