# Generated by Django 4.1.7 on 2023-06-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examsolution', '0030_userprogressrecord_subject_of_paper_written'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprogressrecord',
            options={'ordering': ['-date_completed']},
        ),
        migrations.AddField(
            model_name='userprogressrecord',
            name='user_answer_input',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
