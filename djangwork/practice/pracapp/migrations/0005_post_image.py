# Generated by Django 2.2.3 on 2019-07-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pracapp', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='posts/'),
        ),
    ]