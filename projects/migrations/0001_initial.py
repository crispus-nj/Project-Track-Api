# Generated by Django 4.0.3 on 2022-03-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=30)),
                ('technologies', models.CharField(max_length=500)),
                ('github_link', models.URLField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
