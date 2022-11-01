# Generated by Django 4.1 on 2022-11-01 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_companyprofile_cover_image_and_more'),
        ('activity', '0004_activityprofile_guideline'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='activityprofile',
            name='guideline',
            field=models.ManyToManyField(blank=True, to='company.guideline'),
        ),
    ]
