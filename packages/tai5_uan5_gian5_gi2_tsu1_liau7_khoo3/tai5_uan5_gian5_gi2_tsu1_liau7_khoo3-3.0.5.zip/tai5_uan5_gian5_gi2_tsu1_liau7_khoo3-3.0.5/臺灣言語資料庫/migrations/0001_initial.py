# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import 臺灣言語資料庫.資料模型


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='來源屬性表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('分類', models.CharField(max_length=20)),
                ('性質', models.TextField()),
            ],
            options={
            },
            bases=(models.Model, 臺灣言語資料庫.資料模型.屬性表函式),
        ),
        migrations.CreateModel(
            name='來源表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('名', models.CharField(max_length=100)),
                ('屬性', models.ManyToManyField(to='臺灣言語資料庫.來源屬性表')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='外語表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('收錄時間', models.DateTimeField(auto_now_add=True)),
                ('外語資料', models.TextField()),
                ('來源', models.ForeignKey(to='臺灣言語資料庫.來源表', related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='影音文本表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='影音聽拍表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='影音表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('收錄時間', models.DateTimeField(auto_now_add=True)),
                ('原始影音資料', models.FileField(upload_to='', blank=True)),
                ('網頁影音資料', models.FileField(upload_to='', blank=True)),
                ('來源', models.ForeignKey(to='臺灣言語資料庫.來源表', related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='文本校對表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='文本表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('收錄時間', models.DateTimeField(auto_now_add=True)),
                ('文本資料', models.TextField()),
                ('來源', models.ForeignKey(to='臺灣言語資料庫.來源表', related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='版權表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('版權', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='種類表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('種類', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='翻譯影音表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('外語', models.ForeignKey(to='臺灣言語資料庫.外語表', related_name='翻譯影音')),
                ('影音', models.ForeignKey(unique=True, to='臺灣言語資料庫.影音表', related_name='+')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='翻譯文本表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('外語', models.ForeignKey(to='臺灣言語資料庫.外語表', related_name='翻譯文本')),
                ('文本', models.ForeignKey(unique=True, to='臺灣言語資料庫.文本表', related_name='+')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='聽拍校對表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='聽拍表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('收錄時間', models.DateTimeField(auto_now_add=True)),
                ('聽拍資料', models.TextField()),
                ('來源', models.ForeignKey(to='臺灣言語資料庫.來源表', related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='聽拍規範表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('規範名', models.CharField(unique=True, max_length=20)),
                ('範例', models.TextField()),
                ('說明', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='著作年表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('著作年', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='著作所在地表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('著作所在地', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='語言腔口表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('語言腔口', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='資料屬性表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('分類', models.CharField(db_index=True, max_length=20)),
                ('性質', models.TextField()),
            ],
            options={
            },
            bases=(models.Model, 臺灣言語資料庫.資料模型.屬性表函式),
        ),
        migrations.CreateModel(
            name='資料類型表',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('類型', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='聽拍表',
            name='屬性',
            field=models.ManyToManyField(to='臺灣言語資料庫.資料屬性表'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='聽拍表',
            name='收錄者',
            field=models.ForeignKey(to='臺灣言語資料庫.來源表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='聽拍表',
            name='版權',
            field=models.ForeignKey(to='臺灣言語資料庫.版權表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='聽拍表',
            name='種類',
            field=models.ForeignKey(to='臺灣言語資料庫.種類表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='聽拍表',
            name='著作年',
            field=models.ForeignKey(to='臺灣言語資料庫.著作年表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='聽拍表',
            name='著作所在地',
            field=models.ForeignKey(to='臺灣言語資料庫.著作所在地表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='聽拍表',
            name='規範',
            field=models.ForeignKey(to='臺灣言語資料庫.聽拍規範表', related_name='全部資料'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='聽拍表',
            name='語言腔口',
            field=models.ForeignKey(to='臺灣言語資料庫.語言腔口表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='聽拍校對表',
            name='新聽拍',
            field=models.ForeignKey(unique=True, to='臺灣言語資料庫.聽拍表', related_name='校對資料來源'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='聽拍校對表',
            name='舊聽拍',
            field=models.ForeignKey(to='臺灣言語資料庫.聽拍表', related_name='聽拍校對'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='文本表',
            name='屬性',
            field=models.ManyToManyField(to='臺灣言語資料庫.資料屬性表'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='文本表',
            name='收錄者',
            field=models.ForeignKey(to='臺灣言語資料庫.來源表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='文本表',
            name='版權',
            field=models.ForeignKey(to='臺灣言語資料庫.版權表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='文本表',
            name='種類',
            field=models.ForeignKey(to='臺灣言語資料庫.種類表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='文本表',
            name='著作年',
            field=models.ForeignKey(to='臺灣言語資料庫.著作年表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='文本表',
            name='著作所在地',
            field=models.ForeignKey(to='臺灣言語資料庫.著作所在地表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='文本表',
            name='語言腔口',
            field=models.ForeignKey(to='臺灣言語資料庫.語言腔口表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='文本校對表',
            name='新文本',
            field=models.ForeignKey(unique=True, to='臺灣言語資料庫.文本表', related_name='校對資料來源'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='文本校對表',
            name='舊文本',
            field=models.ForeignKey(to='臺灣言語資料庫.文本表', related_name='文本校對'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音表',
            name='屬性',
            field=models.ManyToManyField(to='臺灣言語資料庫.資料屬性表'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音表',
            name='收錄者',
            field=models.ForeignKey(to='臺灣言語資料庫.來源表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音表',
            name='版權',
            field=models.ForeignKey(to='臺灣言語資料庫.版權表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音表',
            name='種類',
            field=models.ForeignKey(to='臺灣言語資料庫.種類表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音表',
            name='著作年',
            field=models.ForeignKey(to='臺灣言語資料庫.著作年表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音表',
            name='著作所在地',
            field=models.ForeignKey(to='臺灣言語資料庫.著作所在地表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音表',
            name='語言腔口',
            field=models.ForeignKey(to='臺灣言語資料庫.語言腔口表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音聽拍表',
            name='影音',
            field=models.ForeignKey(to='臺灣言語資料庫.影音表', related_name='影音聽拍'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音聽拍表',
            name='聽拍',
            field=models.ForeignKey(unique=True, to='臺灣言語資料庫.聽拍表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音文本表',
            name='影音',
            field=models.ForeignKey(to='臺灣言語資料庫.影音表', related_name='影音文本'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='影音文本表',
            name='文本',
            field=models.ForeignKey(unique=True, to='臺灣言語資料庫.文本表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='外語表',
            name='外語語言',
            field=models.ForeignKey(to='臺灣言語資料庫.語言腔口表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='外語表',
            name='屬性',
            field=models.ManyToManyField(to='臺灣言語資料庫.資料屬性表'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='外語表',
            name='收錄者',
            field=models.ForeignKey(to='臺灣言語資料庫.來源表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='外語表',
            name='版權',
            field=models.ForeignKey(to='臺灣言語資料庫.版權表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='外語表',
            name='種類',
            field=models.ForeignKey(to='臺灣言語資料庫.種類表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='外語表',
            name='著作年',
            field=models.ForeignKey(to='臺灣言語資料庫.著作年表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='外語表',
            name='著作所在地',
            field=models.ForeignKey(to='臺灣言語資料庫.著作所在地表', related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='外語表',
            name='語言腔口',
            field=models.ForeignKey(to='臺灣言語資料庫.語言腔口表', related_name='+'),
            preserve_default=True,
        ),
    ]
