# Generated by Django 3.2.4 on 2022-08-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_APP', '0002_ccboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('pswrd', models.CharField(max_length=200)),
            ],
        ),
    ]