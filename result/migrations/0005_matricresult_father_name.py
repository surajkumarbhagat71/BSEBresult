# Generated by Django 2.2.7 on 2020-02-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_beresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricresult',
            name='father_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
