# Generated by Django 3.1.7 on 2021-03-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20210328_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('', '')], default='', max_length=6),
        ),
    ]