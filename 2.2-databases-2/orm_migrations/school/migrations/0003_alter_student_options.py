# Generated by Django 4.2.7 on 2023-11-22 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_student_teachers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-group'], 'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
    ]