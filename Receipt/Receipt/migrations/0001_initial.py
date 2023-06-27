# Generated by Django 4.2.2 on 2023-06-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(default='2023-01-01')),
                ('standard', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('enrollment_no', models.CharField(max_length=20)),
                ('amount', models.IntegerField(default=0)),
                ('received', models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('card', 'Card')], max_length=50)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], max_length=50)),
                ('signature', models.CharField(max_length=100)),
            ],
        ),
    ]