# Generated by Django 2.2.2 on 2019-06-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0003_auto_20190604_1058")]

    operations = [
        migrations.CreateModel(
            name="OldScholarship",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=256, null=True)),
                ("terms", models.TextField(blank=True, null=True)),
                ("open_time", models.DateTimeField(blank=True, null=True)),
                ("close_time", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"db_table": "scholarships", "managed": False},
        ),
        migrations.CreateModel(
            name="OldScholarshipApplication",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reason", models.TextField(blank=True, null=True)),
                ("terms_accepted", models.BooleanField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"db_table": "scholarship_applications", "managed": False},
        ),
        migrations.DeleteModel(name="Scholarship"),
        migrations.DeleteModel(name="ScholarshipApplication"),
    ]