# Generated by Django 5.0.1 on 2024-01-13 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'permissions': [('export', 'Can export candidate list'), ('notify', 'notify interviewer for candidate review')], 'verbose_name': 'Interviewee', 'verbose_name_plural': 'Interviewees'},
        ),
    ]
