# Generated by Django 3.1 on 2020-08-08 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nave.user')),
            ],
        ),
        migrations.CreateModel(
            name='Naver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('admission_date', models.DateField()),
                ('job_role', models.CharField(choices=[('DEV', 'Desenvolvedor'), ('DES', 'Designer'), ('UXD', 'Designer de UX')], max_length=10)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nave.user')),
                ('projects', models.ManyToManyField(blank=True, default=None, to='nave.Project')),
            ],
        ),
    ]
