# Generated by Django 4.0.6 on 2022-07-28 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_rename_scope_aricle_tabel_alter_scope_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tabel',
            new_name='Scope_Aricle',
        ),
        migrations.RenameField(
            model_name='scope_aricle',
            old_name='tag',
            new_name='scope',
        ),
    ]
