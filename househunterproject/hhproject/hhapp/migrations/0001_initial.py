# Generated by Django 4.1 on 2022-10-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=100)),
                ('hlocation', models.CharField(max_length=100)),
                ('haddress', models.CharField(max_length=100)),
                ('lordname', models.CharField(max_length=100)),
                ('lordcontact', models.CharField(max_length=100)),
                ('ctname', models.CharField(max_length=100)),
                ('ctcontact', models.CharField(max_length=100)),
                ('hmail', models.EmailField(max_length=254)),
                ('depositamount', models.IntegerField()),
                ('rentamount', models.IntegerField()),
                ('apartment', models.CharField(max_length=50)),
                ('cctv', models.BooleanField()),
                ('wifi', models.BooleanField()),
                ('restaurant', models.BooleanField()),
                ('cleaning', models.BooleanField()),
                ('laundry', models.BooleanField()),
                ('gym', models.BooleanField()),
                ('elounge', models.BooleanField()),
                ('parking', models.BooleanField()),
                ('DSTV', models.BooleanField()),
                ('edescription', models.TextField()),
                ('himage', models.ImageField(upload_to='himages/')),
            ],
        ),
    ]
