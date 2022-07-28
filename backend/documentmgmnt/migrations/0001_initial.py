# Generated by Django 4.0.6 on 2022-07-27 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCorrespondence',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('corensonNumner', models.BigIntegerField(verbose_name='Sequence Number')),
                ('coresponDate', models.DateField(verbose_name='Document Date')),
                ('coresponClassification', models.CharField(max_length=1000, verbose_name='Classification')),
                ('coresponSubject', models.CharField(max_length=1000, verbose_name='Subject')),
                ('briefDescription', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Brief Description')),
                ('hasAttachment', models.BooleanField(default=False, verbose_name='Has Attachment')),
                ('actionTakenOn', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Action Taken On')),
                ('isOpen', models.BooleanField(default=True, verbose_name='Is Open')),
                ('fileName', models.CharField(blank=True, max_length=255, null=True, verbose_name='File Name')),
                ('filePath', models.CharField(blank=True, max_length=255, null=True, verbose_name='File Path')),
                ('fileType', models.CharField(blank=True, max_length=15, null=True, verbose_name='File Type')),
                ('remarks', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Remarks')),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('modifiedOn', models.DateTimeField(blank=True, null=True, verbose_name='Modified On')),
                ('coresponType', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.documentnumberformat')),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projcoresp_createdBy', to=settings.AUTH_USER_MODEL)),
                ('modifiedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectcoresp_modifiedBy', to=settings.AUTH_USER_MODEL)),
                ('prjId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.projectmaster')),
            ],
            options={
                'verbose_name_plural': 'ProjectCorrespondences',
                'ordering': ['prjId', 'coresponType', 'corensonNumner'],
                'unique_together': {('prjId', 'coresponType', 'corensonNumner')},
            },
        ),
    ]
