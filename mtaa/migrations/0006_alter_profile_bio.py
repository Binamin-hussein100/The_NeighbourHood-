# Generated by Django 3.2.7 on 2021-09-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa', '0005_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Words that defend you when you are not there to defend yourself'),
        ),
    ]