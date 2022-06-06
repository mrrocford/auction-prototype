# Generated by Django 4.0.4 on 2022-05-29 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_product_delete_auction_delete_auction_bid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_bids', models.IntegerField()),
                ('time_starting', models.DateTimeField()),
                ('time_ending', models.DateTimeField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.product')),
            ],
        ),
    ]
