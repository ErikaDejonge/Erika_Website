# Generated by Django 5.0.7 on 2024-09-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ErikaApp', '0012_alter_bookerika_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Downloaded_Email', models.EmailField(max_length=254)),
            ],
        ),
    ]