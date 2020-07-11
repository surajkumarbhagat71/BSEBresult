# Generated by Django 2.2.7 on 2020-02-20 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_auto_20200218_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('img', models.ImageField(upload_to='media/')),
                ('dob', models.DateField()),
                ('roll_no', models.IntegerField()),
                ('roll_code', models.IntegerField()),
                ('marks', models.IntegerField(default=0)),
                ('renk', models.IntegerField(default=0)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.Gender')),
            ],
        ),
    ]
