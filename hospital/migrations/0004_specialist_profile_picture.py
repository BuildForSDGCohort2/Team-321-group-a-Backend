# Generated by Django 3.0 on 2020-10-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20201009_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='doc_image/'),
        ),
    ]
