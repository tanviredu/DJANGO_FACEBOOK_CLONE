# Generated by Django 5.0.4 on 2024-04-23 07:56

import django.db.models.deletion
import shortuuid.django_fields
import userauth.db.Profile
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvwxyz0123456789",
                        length=7,
                        max_length=25,
                        prefix="",
                    ),
                ),
                (
                    "cover_img",
                    models.ImageField(
                        default="cover.jpg",
                        upload_to=userauth.db.Profile.user_directory_path,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="default.jpg",
                        upload_to=userauth.db.Profile.user_directory_path,
                    ),
                ),
                ("fullname", models.CharField(blank=True, max_length=200, null=True)),
                ("phone", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("female", "Female"), ("male", "Male")],
                        default="male",
                        max_length=100,
                    ),
                ),
                (
                    "relationship",
                    models.CharField(
                        choices=[("single", "Single"), ("Married", "Married")],
                        default="Single",
                        max_length=100,
                    ),
                ),
                ("bio", models.CharField(blank=True, max_length=200, null=True)),
                ("about_me", models.TextField(blank=True, null=True)),
                ("country", models.CharField(blank=True, max_length=200, null=True)),
                ("state", models.CharField(blank=True, max_length=200, null=True)),
                ("city", models.CharField(blank=True, max_length=200, null=True)),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                ("working_at", models.CharField(blank=True, max_length=200, null=True)),
                ("instagram", models.CharField(blank=True, max_length=200, null=True)),
                ("whatsapp", models.CharField(blank=True, max_length=200, null=True)),
                ("veriifed", models.BooleanField(default=False)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "blocked",
                    models.ManyToManyField(
                        blank=True, related_name="blocked", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "folllowers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="followers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "following",
                    models.ManyToManyField(
                        blank=True,
                        related_name="following",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "friends",
                    models.ManyToManyField(
                        blank=True, related_name="friends", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
