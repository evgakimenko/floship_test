# Generated by Django 4.2.2 on 2023-06-28 07:57

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_name', models.CharField(max_length=255)),
                ('order_status',
                 models.IntegerField(choices=[(0, 'Open'), (1, 'In Progress'), (2, 'Closed')])),
            ],
        ),
    ]
