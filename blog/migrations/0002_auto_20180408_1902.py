# Generated by Django 2.0.2 on 2018-04-08 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date']},
        ),
    ]
