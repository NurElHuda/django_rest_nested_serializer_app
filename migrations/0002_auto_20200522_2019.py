# Generated by Django 3.0.6 on 2020-05-22 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_nested_serializer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='sign_up_date',
            new_name='last_login_date',
        ),
    ]
