# Generated by Django 3.1.7 on 2021-04-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210430_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default="static 'img/bram-naus-n8Qb1ZAkK88-unsplash.jpg'", null=True, upload_to='profile/'),
        ),
    ]
