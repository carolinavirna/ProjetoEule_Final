# Generated by Django 3.2.13 on 2022-05-27 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220527_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questao_Classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classificacao')),
                ('id_quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questoes')),
            ],
        ),
    ]