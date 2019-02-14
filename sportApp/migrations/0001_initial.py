# Generated by Django 2.1.7 on 2019-02-14 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl', models.CharField(max_length=1)),
                ('wday', models.CharField(max_length=13)),
                ('tday', models.CharField(max_length=4)),
                ('countmax', models.CharField(max_length=4)),
                ('countnow', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportApp.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tabnum', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='type1',
            fields=[
                ('contacts', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sportApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='type2',
            fields=[
                ('email', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=7)),
                ('goal', models.CharField(max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sportApp.user')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sportApp.place'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportApp.sport'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sportApp.type1'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='stud',
            field=models.ManyToManyField(to='sportApp.type2'),
        ),
    ]
