# Generated by Django 5.2.2 on 2025-06-11 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmc_proxy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('base_asset', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='基础资产')),
                ('symbol', models.CharField(db_index=True, max_length=50, verbose_name='最优交易对符号')),
                ('quote_asset', models.CharField(db_index=True, max_length=20, verbose_name='最优计价资产')),
                ('exchange', models.CharField(db_index=True, max_length=50, verbose_name='最优交易所')),
                ('price', models.DecimalField(decimal_places=8, max_digits=20, verbose_name='最优价格')),
                ('price_change_24h', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='24小时价格变化率(%)')),
                ('volume_24h', models.DecimalField(blank=True, decimal_places=8, max_digits=30, null=True, verbose_name='24小时成交量')),
                ('exchange_priority', models.PositiveIntegerField(default=999, verbose_name='交易所优先级')),
                ('quote_priority', models.PositiveIntegerField(default=999, verbose_name='稳定币优先级')),
                ('price_timestamp', models.DateTimeField(db_index=True, verbose_name='价格时间戳')),
                ('cmc_asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asset_prices', to='cmc_proxy.cmcasset', verbose_name='CMC资产关联')),
            ],
            options={
                'verbose_name': '资产价格',
                'verbose_name_plural': '资产价格',
                'db_table': 'asset_prices',
                'indexes': [models.Index(fields=['base_asset'], name='asset_price_base_as_05a00e_idx'), models.Index(fields=['exchange_priority', 'quote_priority'], name='asset_price_exchang_276bbe_idx'), models.Index(fields=['price_timestamp'], name='asset_price_price_t_b85b26_idx')],
            },
        ),
    ]
