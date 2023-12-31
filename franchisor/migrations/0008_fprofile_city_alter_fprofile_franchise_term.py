# Generated by Django 4.1.3 on 2023-05-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("franchisor", "0007_fprofile_logo_fprofile_employees_requires_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="fprofile",
            name="city",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="fprofile",
            name="franchise_term",
            field=models.IntegerField(null=True),
        ),
    ]
