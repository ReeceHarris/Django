# Generated by Django 3.1.7 on 2021-04-01 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_auto_20210331_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(blank=True, choices=[('Mrs.', 'Mrs.'), ('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('', '')], default='', max_length=6),
        ),
    ]
