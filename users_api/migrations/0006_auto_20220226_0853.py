# Generated by Django 3.2.12 on 2022-02-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0005_auto_20220226_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='company_address',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_city',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_district',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_neighborhood',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_official_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_sign_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_tax_administration',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_tax_id',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='getiryemek_api_key',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='getiryemek_api_secret',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='identity_id',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='trendyolyemek_api_key',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='trendyolyemek_api_secret',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='yemeksepeti_api_key',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='yemeksepeti_api_secret',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]