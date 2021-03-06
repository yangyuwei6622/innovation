# Generated by Django 3.0.3 on 2020-03-08 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qingShang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tTitle', models.CharField(max_length=30)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uAddress',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uEmployer',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uPhoneNum',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.CreateModel(
            name='shopInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sTitle', models.CharField(max_length=50)),
                ('sPic', models.ImageField(upload_to='shops')),
                ('sPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('isDelete', models.BooleanField(default=False)),
                ('sUnit', models.CharField(max_length=50)),
                ('sStar', models.IntegerField()),
                ('sContent', models.CharField(max_length=600)),
                ('sBrief', models.CharField(max_length=200)),
                ('sType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qingShang.TypeInfo')),
            ],
        ),
    ]
