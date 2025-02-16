# Generated by Django 3.2.18 on 2023-03-04 04:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20230302_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_paid', models.DateField(auto_now=True)),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(30000)])),
                ('dues', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RoomChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='hostel',
        ),
        migrations.RemoveField(
            model_name='warden',
            name='hostel',
        ),
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='present',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AddField(
            model_name='student',
            name='fee_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='room_alloted',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Hostel',
        ),
        migrations.AddField(
            model_name='roomchange',
            name='new_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='new', to='management.room'),
        ),
        migrations.AddField(
            model_name='roomchange',
            name='old_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='old', to='management.room'),
        ),
        migrations.AddField(
            model_name='roomchange',
            name='requester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.student'),
        ),
        migrations.AddField(
            model_name='fee',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.student'),
        ),
    ]
