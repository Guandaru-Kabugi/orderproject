# Generated by Django 5.1.1 on 2024-10-06 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0002_order_additional_notes_order_page_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notified', models.BooleanField(default=False, verbose_name='notification of order')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.order')),
            ],
        ),
    ]
