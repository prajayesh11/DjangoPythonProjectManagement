# Generated by Django 3.1 on 2020-09-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200914_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, choices=[('FREE', 'Free'), ('INPROGRESS', 'In-Progress'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='NEW', max_length=255, null=True),
        ),
    ]
