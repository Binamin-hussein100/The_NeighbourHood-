# Generated by Django 3.2.7 on 2021-09-28 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa', '0002_alter_user_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mtaa.neigbourhood'),
        ),
    ]
