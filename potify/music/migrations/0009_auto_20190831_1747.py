# Generated by Django 2.1.7 on 2019-09-01 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20190719_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='name',
            new_name='title',
        ),
    ]
