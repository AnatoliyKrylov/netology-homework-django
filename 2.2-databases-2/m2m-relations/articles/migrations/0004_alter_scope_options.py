# Generated by Django 4.2.7 on 2023-11-22 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tag_options_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['is_main']},
        ),
    ]
