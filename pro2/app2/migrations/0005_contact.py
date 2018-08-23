# Generated by Django 2.0.5 on 2018-07-24 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_document_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('feed', models.CharField(max_length=200)),
                ('radio', models.CharField(max_length=128)),
            ],
        ),
    ]