# Generated by Django 4.2.1 on 2023-05-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.EmailField(default=1, max_length=255, verbose_name='name'),
            preserve_default=False,
        ),
    ]