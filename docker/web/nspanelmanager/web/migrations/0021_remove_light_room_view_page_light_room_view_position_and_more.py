# Generated by Django 4.1.7 on 2023-04-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_roomviewpagelight_light_room_view_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='light',
            name='room_view_page',
        ),
        migrations.AddField(
            model_name='light',
            name='room_view_position',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='RoomViewPageLight',
        ),
    ]
