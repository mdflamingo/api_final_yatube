# Generated by Django 3.2.16 on 2023-05-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230520_1101'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_author_user_following',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_user_following'),
        ),
    ]
