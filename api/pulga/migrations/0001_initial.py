# Generated by Django 2.2.2 on 2019-06-16 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.IntegerField()),
                ('street', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=15)),
                ('zip_code', models.CharField(max_length=20)),
                ('extra_information', models.CharField(blank=True, max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('bids_id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_stamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('items_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pulga.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('phones_id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sales_id', models.AutoField(primary_key=True, serialize=False)),
                ('done', models.BooleanField()),
                ('initial_price', models.IntegerField()),
                ('post_date', models.DateTimeField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pulga.Items')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('sales_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pulga.Sales')),
            ],
            bases=('pulga.sales',),
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('sales_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pulga.Sales')),
            ],
            bases=('pulga.sales',),
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('sales_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pulga.Sales')),
            ],
            bases=('pulga.sales',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('nickname', models.CharField(max_length=20)),
                ('addresses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulga.Addresses')),
                ('phones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulga.Phones')),
            ],
        ),
        migrations.CreateModel(
            name='AuctionSale',
            fields=[
                ('sales_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pulga.Sales')),
                ('duration', models.IntegerField()),
                ('bids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulga.Bids')),
            ],
            bases=('pulga.sales',),
        ),
    ]