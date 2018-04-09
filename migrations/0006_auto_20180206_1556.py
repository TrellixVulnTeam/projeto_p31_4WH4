# Generated by Django 2.0 on 2018-02-06 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projeto_p3', '0005_auto_20180206_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipamentos_empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empreiteiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp1', to='projeto_p3.empreiteiros')),
            ],
        ),
        migrations.CreateModel(
            name='sub_empreiteiros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=500)),
                ('morada', models.CharField(max_length=500)),
                ('atividade', models.CharField(max_length=500)),
                ('alvara', models.CharField(max_length=500)),
                ('nif', models.CharField(max_length=500)),
                ('nome_representante', models.CharField(max_length=500)),
                ('contacto_representante', models.CharField(max_length=500)),
                ('num_ap_seguro_resp_civil', models.CharField(max_length=500)),
                ('data_seguro_resp_civil', models.DateField()),
                ('validade_seguro_resp_civil', models.CharField(max_length=500)),
                ('data_decl_ss', models.DateField()),
                ('validade_decl_ss', models.CharField(max_length=500)),
                ('data_cert_financas', models.DateField()),
                ('validade_cert_financas', models.CharField(max_length=500)),
                ('mes_folha_ferias', models.CharField(choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'), ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Dezembro', 'Dezembro')], max_length=500)),
                ('recibo_folha_ferias', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=500)),
                ('horario_trabalho', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=500)),
                ('declaracao_pss', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=500)),
                ('declaracao_imigrantes', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=500)),
                ('contrato_subempreitada', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=500)),
                ('empreiteiros', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empre2', to='projeto_p3.empreiteiros')),
            ],
        ),
        migrations.RemoveField(
            model_name='equipamentos',
            name='empreiteiro',
        ),
        migrations.AddField(
            model_name='equipamentos',
            name='carro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carros1', to='projeto_p3.carros'),
        ),
        migrations.AddField(
            model_name='equipamentos',
            name='cartao_combustivel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pc', to='projeto_p3.cartao_comb'),
        ),
        migrations.AddField(
            model_name='equipamentos',
            name='outros',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='equipamentos',
            name='portatil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pc', to='projeto_p3.portatil'),
        ),
        migrations.AddField(
            model_name='equipamentos',
            name='telemovel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tele', to='projeto_p3.telemovel'),
        ),
        migrations.AddField(
            model_name='equipamentos',
            name='utilizador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='utilizador', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
