# Generated by Django 3.0 on 2020-10-12 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_specialist_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialist',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='user',
            name='account',
        ),
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_death',
        ),
        migrations.AddField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, help_text='Enter the date of birth', null=True)),
                ('date_of_death', models.DateField(blank=True, help_text='Enter the date of death', null=True)),
                ('Address', models.CharField(help_text='Enter the address', max_length=100, null=True)),
                ('account', models.ForeignKey(blank=True, help_text='The account details', null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Payment')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
