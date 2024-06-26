# Generated by Django 5.0.1 on 2024-05-21 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0002_rename_numer_of_questions_quiz_number_of_questions_and_more"),
        ("quiz_questions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="quiz",
            field=models.ForeignKey(
                help_text="case des quiz (les choix)",
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.quiz",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="text",
            field=models.CharField(help_text="Questions de quiz", max_length=255),
        ),
    ]
