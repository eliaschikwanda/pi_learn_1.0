# Generated by Django 4.1.7 on 2023-05-14 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examsolution', '0012_fullquestionanswer_paper_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullquestionanswer',
            name='paper_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examsolution.paper'),
        ),
    ]
