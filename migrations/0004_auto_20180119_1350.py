# Generated by Django 2.0 on 2018-01-19 13:50

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_p3', '0003_auto_20180119_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='descricao',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='conformidade_texto', chained_model_field='lista', on_delete=django.db.models.deletion.CASCADE, to='projeto_p3.descricao_conformidades'),
        ),
    ]
