# Generated by Django 2.2.4 on 2019-09-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='occupants_count',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.AddField(
            model_name='business',
            name='logo',
            field=models.ImageField(blank=True, default='', max_length=255, null=True, upload_to='business/'),
        ),
        migrations.AddField(
            model_name='business',
            name='website',
            field=models.URLField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='', max_length=255, null=True, upload_to='profile/'),
        ),
    ]
