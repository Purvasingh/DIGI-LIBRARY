# Generated by Django 2.0.5 on 2018-07-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='subject',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]