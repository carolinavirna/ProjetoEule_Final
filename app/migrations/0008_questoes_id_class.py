# Generated by Django 3.2.13 on 2022-05-27 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_questao_classificacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='questoes',
            name='id_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.classificacao'),
            preserve_default=False,
        ),
    ]