# Generated by Django 3.0.8 on 2020-07-22 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0006_auto_20200722_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=400)),
                ('data_criacao', models.DateTimeField(auto_now=True)),
                ('curtidas', models.ManyToManyField(related_name='curtidas', to='pessoa.Perfil')),
                ('repiados', models.ManyToManyField(related_name='repiados', to='pessoa.Perfil')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='piados', to='pessoa.Perfil')),
            ],
        ),
    ]
