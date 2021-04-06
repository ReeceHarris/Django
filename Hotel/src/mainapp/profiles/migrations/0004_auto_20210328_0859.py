# Generated by Django 3.1.7 on 2021-03-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profiles_prefix_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='PREFIX_CHOICES',
        ),
        migrations.AddField(
            model_name='profiles',
            name='type',
            field=models.CharField(blank=True, choices=[('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('Mr.', 'Mr.')], default='', max_length=6),
        ),
    ]