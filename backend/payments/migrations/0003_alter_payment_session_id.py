# Generated by Django 4.2.7 on 2023-11-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0002_rename_type_payment_type_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="session_id",
            field=models.CharField(max_length=150),
        ),
    ]