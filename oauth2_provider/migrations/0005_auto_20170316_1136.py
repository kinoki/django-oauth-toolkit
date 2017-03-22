# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0004_auto_20160525_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='allowed_scopes',
            field=models.TextField(blank=True, help_text='Scopes that requested application can allow'),
        ),
    ]