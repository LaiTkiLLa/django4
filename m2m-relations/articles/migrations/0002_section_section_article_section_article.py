# Generated by Django 4.0.6 on 2022-07-18 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.CreateModel(
            name='Section_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='articles.article')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='articles.section')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='article',
            field=models.ManyToManyField(through='articles.Section_Article', to='articles.article'),
        ),
    ]
