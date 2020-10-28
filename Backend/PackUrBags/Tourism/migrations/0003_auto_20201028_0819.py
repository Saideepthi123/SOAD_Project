# Generated by Django 3.0.5 on 2020-10-28 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
        ('tourism', '0002_booking_city_monument_monumentinfo_payment_userhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guide_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_guide_email', to='guide.GuideData'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='guide_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_guide_email', to='guide.GuideData'),
        ),
        migrations.DeleteModel(
            name='GuideData',
        ),
    ]
