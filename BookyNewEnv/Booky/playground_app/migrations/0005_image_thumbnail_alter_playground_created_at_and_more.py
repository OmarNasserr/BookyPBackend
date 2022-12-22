# Generated by Django 4.1.4 on 2022-12-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playground_app", "0004_alter_playground_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="thumbnail",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="playground",
            name="created_at",
            field=models.CharField(
                default="19 Dec, 2022 - 04h53m14 PM", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="playground",
            name="updated_at",
            field=models.CharField(
                default="19 Dec, 2022 - 04h53m14 PM", max_length=100
            ),
        ),
    ]