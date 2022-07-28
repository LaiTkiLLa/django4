# Generated by Django 4.0.6 on 2022-07-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_rename_is_main_scope_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='name',
            new_name='tag_name',
        ),
        migrations.RemoveField(
            model_name='article',
            name='scope',
        ),
        migrations.AddField(
            model_name='scope_aricle',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
