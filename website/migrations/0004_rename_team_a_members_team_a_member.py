# Generated by Django 5.1.2 on 2024-11-02 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_team_a_member_team_a_members'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Team_A_Members',
            new_name='Team_A_Member',
        ),
    ]