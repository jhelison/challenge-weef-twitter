# Generated by Django 3.2.8 on 2021-10-13 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211013_1700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userfollowing',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('user_id', 'following_user_id')},
        ),
    ]
