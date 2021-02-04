# Generated by Django 3.1.5 on 2021-02-03 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20210129_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_scrapped',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='merchant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='test_app.merchant'),
        ),
    ]