# Generated by Django 2.2.7 on 2019-12-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealerApp', '0005_product_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('enquiry_note', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
