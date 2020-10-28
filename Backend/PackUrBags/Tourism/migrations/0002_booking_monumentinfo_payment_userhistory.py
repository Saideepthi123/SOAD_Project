# Generated by Django 3.0.4 on 2020-10-24 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tourism', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Booked at ')),
                ('guide_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_guide_email', to='Tourism.GuideData')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_user_email', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_of_payment', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Booked at ')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_user_email', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('mode_of_payment', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Booked at ')),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_booking_id', to='Tourism.Booking')),
                ('guide_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_guide_email', to='Tourism.GuideData')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_user_email', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MonumentInfo',
            fields=[
                ('monument_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('monument_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tourism.Monument')),
            ],
        ),
    ]