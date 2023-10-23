# Generated by Django 4.0.3 on 2022-04-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_addcomplaint_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcomplaint',
            name='category',
            field=models.IntegerField(choices=[(1, 'Accident'), (2, 'Fraud'), (3, 'Robbery'), (4, 'Missing'), (5, 'Cyber Crime'), (6, 'Other')], default=1, max_length=60),
        ),
    ]
