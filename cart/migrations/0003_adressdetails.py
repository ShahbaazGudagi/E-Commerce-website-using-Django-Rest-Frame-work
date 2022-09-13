# Generated by Django 4.0.6 on 2022-07-20 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_alter_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdressDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.TextField()),
                ('Phone_no', models.PositiveIntegerField(max_length=10)),
                ('pin_code', models.PositiveIntegerField(max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]