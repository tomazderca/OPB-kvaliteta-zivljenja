# Generated by Django 3.0.8 on 2020-08-23 16:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField()),
                ('url', models.URLField()),
                ('likes', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stili',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('stil', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='umetnik',
            name='year_of_birth',
            field=models.DateField(verbose_name='birth'),
        ),
        migrations.AlterField(
            model_name='umetnik',
            name='year_of_death',
            field=models.DateField(verbose_name='death'),
        ),
        migrations.AlterField(
            model_name='umetnina',
            name='year',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2020)]),
        ),
        migrations.CreateModel(
            name='UserDescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('content', models.TextField()),
                ('artwork_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Arts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArtworksTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Arts')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Tags')),
            ],
        ),
    ]
