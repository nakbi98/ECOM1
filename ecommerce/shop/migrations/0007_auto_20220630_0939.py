# Generated by Django 2.2.12 on 2022-06-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='avis',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=150),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(max_length=500),
        ),
    ]