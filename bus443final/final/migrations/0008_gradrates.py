# Generated by Django 2.2.7 on 2019-12-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0007_auto_20191212_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='gradrates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campus', models.CharField(max_length=100)),
                ('GradYear', models.IntegerField()),
                ('Year4', models.FloatField()),
                ('Year5', models.FloatField()),
                ('Year6', models.FloatField()),
            ],
        ),
    ]
