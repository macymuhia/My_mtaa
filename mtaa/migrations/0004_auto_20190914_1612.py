# Generated by Django 2.2.4 on 2019-09-14 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa', '0003_auto_20190914_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mtaa.UserProfile'),
        ),
    ]
