# Generated by Django 3.1.6 on 2021-02-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anke', '0002_auto_20210204_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='anke',
            name='age',
            field=models.PositiveIntegerField(choices=[('m', '男性'), ('f', '女性')], null=True, verbose_name='年齢'),
        ),
        migrations.AddField(
            model_name='anke',
            name='sex',
            field=models.CharField(max_length=200, null=True, verbose_name='性別'),
        ),
        migrations.AddField(
            model_name='anke',
            name='shop',
            field=models.CharField(choices=[('ka', 'カパテリア'), ('be', '紅乙女酒造'), ('ky', '巨峰ワイン'), ('ju', '樹蘭マルシェ')], max_length=300, null=True, verbose_name='お店'),
        ),
        migrations.AlterField(
            model_name='anke',
            name='question3',
            field=models.CharField(blank=True, choices=[('m-car', 'マイカー'), ('r-car', 'レンタカー'), ('jr', 'ＪＲ'), ('r-bus', '路線バス'), ('s-bus', '観光バス'), ('others', 'その他')], max_length=200, null=True, verbose_name='質問③'),
        ),
    ]