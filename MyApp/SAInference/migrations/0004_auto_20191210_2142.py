# Generated by Django 3.0 on 2019-12-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAInference', '0003_auto_20191210_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentimentanalysisinference',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
