# Generated by Django 3.2.5 on 2021-11-19 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_displaypage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='description',
        ),
    ]
