# Generated by Django 3.2 on 2022-06-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='d', upload_to=''),
            preserve_default=False,
        ),
    ]