# Generated by Django 3.1.6 on 2021-02-10 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anke', '0017_auto_20210210_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anke',
            name='age',
            field=models.CharField(blank=True, choices=[('0', '20歳未満'), ('1', '20歳以上〜30歳未満'), ('2', '30歳以上〜40歳未満'), ('3', '40歳以上〜50歳未満'), ('4', '50歳以上〜60歳未満'), ('6', '60歳以上〜70歳未満'), ('7', '70歳以上')], max_length=200, null=True, verbose_name='年代'),
        ),
    ]