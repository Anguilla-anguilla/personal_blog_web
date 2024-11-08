# Generated by Django 4.2.16 on 2024-10-28 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_article_options_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, verbose_name='username')),
                ('comment', models.TextField(verbose_name='comment')),
                ('date', models.DateTimeField(verbose_name='comment creation date')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.article', verbose_name='article')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
