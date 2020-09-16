# Generated by Django 3.1 on 2020-09-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200914_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('NA', 'NA'), ('DEVELOPER', 'Developer'), ('TEAMLEAD', 'Team Leader'), ('PROJECTMANAGER', 'Project Manager')], default='NA', max_length=255, null=True),
        ),
    ]
