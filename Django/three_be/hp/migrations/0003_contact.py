# Generated by Django 3.2 on 2021-06-04 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0002_alter_blog_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_date', models.DateField(help_text='※', verbose_name='ご希望日（第一希望）')),
                ('first_time', models.DateTimeField(help_text='※', verbose_name='ご希望時間帯（第一希望）')),
                ('second_date', models.DateField(blank=True, null=True, verbose_name='ご希望日（第二希望）')),
                ('second_time', models.DateTimeField(blank=True, help_text='※', null=True, verbose_name='ご希望時間帯（第二希望）')),
                ('parent_name', models.CharField(blank=True, help_text='※', max_length=50, null=True, verbose_name='保護者氏名')),
                ('student_name', models.CharField(help_text='※', max_length=50, verbose_name='生徒名')),
                ('birthday', models.DateField(help_text='※', verbose_name='生年月日')),
                ('phone_number', models.CharField(help_text='※', max_length=12, verbose_name='電話番号')),
                ('email', models.EmailField(help_text='※', max_length=254, verbose_name='メールアドレス')),
                ('text', models.CharField(blank=True, max_length=200, null=True, verbose_name='ご要望・ご質問')),
            ],
        ),
    ]