# Generated by Django 4.2.16 on 2024-11-03 20:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_categories_article_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='text'),
        ),
    ]
