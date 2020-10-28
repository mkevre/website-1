# Generated by Django 2.2.16 on 2020-10-28 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_quote_quote', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='content',
            field=models.TextField(default='', verbose_name='Quote'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='style',
            field=models.CharField(choices=[('standard', 'Standard'), ('carousel', 'Carousel')], default='standard', max_length=50, verbose_name='Style'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='target',
            field=models.CharField(blank=True, choices=[('_blank', 'New window')], default='_blank', max_length=50, verbose_name='Target'),
        ),
    ]
