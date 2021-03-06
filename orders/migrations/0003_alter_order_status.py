# Generated by Django 3.2.3 on 2021-07-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'Формируется'), ('STR', 'Отправлен в обработку'), ('PRD', 'Обработан'), ('PD', 'Оплачен'), ('RD', 'Готов к выдаче'), ('CNC', 'Отменён'), ('DVD', 'Выдан')], default='FM', max_length=3, verbose_name='Cтатус'),
        ),
    ]
