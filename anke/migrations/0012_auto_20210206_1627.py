# Generated by Django 3.1.6 on 2021-02-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anke', '0011_auto_20210206_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anke',
            name='shop',
            field=models.CharField(choices=[('ka', 'カパテリア'), ('be', '紅乙女酒造'), ('ky', '巨峰ワイン'), ('ju', '樹蘭マルシェ'), ('others', 'その他')], default='others', max_length=300, verbose_name='お店'),
        ),
    ]