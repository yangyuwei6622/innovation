# Generated by Django 3.0.3 on 2020-03-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uName', models.CharField(max_length=20)),
                ('uPwd', models.CharField(max_length=60)),
                ('uEmail', models.CharField(max_length=60)),
                ('uEmployer', models.CharField(max_length=20)),
                ('uAddress', models.CharField(max_length=60)),
                ('uPhoneNum', models.CharField(max_length=11)),
            ],
        ),
    ]
