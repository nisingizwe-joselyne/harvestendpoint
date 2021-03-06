# Generated by Django 3.1.6 on 2021-03-14 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210310_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('dateofbirth', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('Cooperative', models.CharField(max_length=255)),
                ('farmercode', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='profilecooperative',
            old_name='farmer',
            new_name='farmers',
        ),
        migrations.AddField(
            model_name='cooperative',
            name='district',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='harvesttype',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='leaderphone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilecooperative',
            name='activate_on',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='recorder',
            name='cooperativename',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.cooperative'),
            preserve_default=False,
        ),
    ]
