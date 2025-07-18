# Generated by Django 5.2 on 2025-05-23 22:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0001_initial'),
        ('diagnosis', '0001_initial'),
        ('patient_form', '0002_alter_patient_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('CLOSED', 'Closed')], default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('diagnosis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_sessions', to='diagnosis.diagnosis')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_sessions', to='patient_form.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_sessions', to='patient_form.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to=settings.AUTH_USER_MODEL)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='consultation.chatsession')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
