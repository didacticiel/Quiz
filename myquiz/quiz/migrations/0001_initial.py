# Generated by Django 5.0.1 on 2024-02-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quiz",
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
                ("name", models.CharField(max_length=120)),
                ("topic", models.CharField(max_length=120)),
                ("numer_of_questions", models.IntegerField()),
                ("time", models.IntegerField(help_text="Durée du quizz en minutes")),
                (
                    "required_score_to_pass",
                    models.IntegerField(help_text="Score requise en %"),
                ),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("facile", "facile"),
                            ("moyen", "moyen"),
                            ("difficile", "difficile"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Quizes",},
        ),
    ]
