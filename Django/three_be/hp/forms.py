from django import forms
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget
from .models import Blog, Post, Contact
from three_be import settings
from . import widgets
import datetime


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ('created_at',)
        widgets = {
            'text': SummernoteWidget(),
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('created_at',)
        widgets = {
            'text': SummernoteWidget(),
        }


class ContactForm(forms.ModelForm):
    # first_date = forms.DateField(input_formats=settings.DATETIME_INPUT_FORMATS)
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['first_time'] = forms.DateTimeField(label='ご希望時間帯（第一希望）', widget=forms.Select(), input_formats='%Y-%m-%d %H:%M:%S')
        self.label_suffix = ""
        local_now = timezone.localtime()

        times = (
            # (local_now.replace(hour=0, minute=0, second=0).strftime(
            # '%H:%M') , '選択してください'),
            (local_now.replace(hour=10, minute=30, second=0).strftime(
            '%H:%M') , '10:30'),
            (local_now.replace(hour=13, minute=0, second=0).strftime(
            '%H:%M') , '13:00'),
            (local_now.replace(hour=15, minute=20, second=0).strftime(
            '%H:%M') , '15:20'),
            (local_now.replace(hour=16, minute=20, second=0).strftime(
            '%H:%M') , '16:20'),
            (local_now.replace(hour=17, minute=20, second=0).strftime(
            '%H:%M') , '17:20'),
            (local_now.replace(hour=18, minute=20, second=0).strftime(
            '%H:%M') , '18:20'),
            (local_now.replace(hour=19, minute=20, second=0).strftime(
            '%H:%M') , '19:20'),
         )
        months = {
            1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11', 12: '12'
        }
        self.fields['first_date'] = forms.DateField(label='ご希望日（第一希望）', input_formats=settings.DATETIME_INPUT_FORMATS)
        self.fields['first_time'] = forms.DateTimeField(label='ご希望時間帯（第一希望）', input_formats=settings.DATETIME_INPUT_FORMATS)
        self.fields['first_time'].widget = forms.Select(choices=times)
        self.fields['second_date'] = forms.DateField(label='ご希望日（第二希望）', input_formats=settings.DATETIME_INPUT_FORMATS)
        self.fields['second_time'] = forms.DateTimeField(label='ご希望時間帯（第二希望）', input_formats=settings.DATETIME_INPUT_FORMATS)
        self.fields['second_time'].widget = forms.Select(choices=times)
        self.fields['birthday'] = forms.DateField(label='生年月日', input_formats=settings.DATETIME_INPUT_FORMATS)
        self.fields['birthday'].widget = widgets.SelectDateWidget(years=[x for x in range(1950, 2030)], months=months)
        self.fields['phone_number'].widget = forms.TextInput(attrs={'placeholder': '例：11122223333（半角）'})
        self.fields['text'].widget = forms.Textarea(attrs={'placeholder':'ご要望・ご質問があれば、気軽にどうぞ'})
# class ContactForm(forms.Form):
#     first_date = forms.DateField(
#         label='ご希望日（第一希望）', required=True,
#         help_text='※'
#         )
#
#     first_time = forms.DateTimeField(
#         label='ご希望時間帯（第一希望）', required=True,
#         help_text='※', widget=forms.Select()
#     )
#
#     second_date = forms.DateField(
#         label='ご希望日（第二希望）', required=False
#     )
#
#     second_time = forms.DateTimeField(
#     label='ご希望時間帯（第二希望）', required=False,
#     help_text='※', widget=forms.Select()
#     )
#
#     parent_name = forms.CharField(
#         label='保護者氏名', max_length=50,
#         required=False, help_text='※'
#     )
#
#     student_name = forms.CharField(
#         label='生徒名', max_length=50,
#         required=True, help_text='※'
#     )
#
#     birthday = forms.DateField(
#         label='生年月日',
#         widget=forms.SelectDateWidget(years=[x for x in range(1950, 2030)])
#         )
#
#     phone_number = forms.CharField(
#         label='電話番号', max_length=12,
#         required=True, help_text='※',
#         widget=forms.TextInput(attrs={'placeholder':'例：11122223333（半角）'})
#     )
#
#     email = forms.EmailField(
#         label='メールアドレス', required=True,
#         help_text='※'
#     )
#
#     text = forms.CharField(
#         label='ご要望・ご質問',
#         widget=forms.Textarea(attrs={'placeholder':'ご要望・ご質問があれば、気軽にどうぞ'}),
#         required=False
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.label_suffix = ""
#         local_now = timezone.localtime()
#         times = (
#             (local_now.replace(hour=0, minute=0, second=0).strftime(
#             '%Y-%m-%d %H:%M:%S') , '選択してください'),
#             (local_now.replace(hour=0, minute=0, second=0).strftime(
#             '%Y-%m-%d %H:%M:%S') , '10時30分'),
#             (local_now.replace(hour=0, minute=0, second=0).strftime(
#             '%Y-%m-%d %H:%M:%S') , '13時00分'),
#             (local_now.replace(hour=0, minute=0, second=0).strftime(
#             '%Y-%m-%d %H:%M:%S') , '15時20分'),
#             (local_now.replace(hour=0, minute=0, second=0).strftime(
#             '%Y-%m-%d %H:%M:%S') , '16時20分'),
#             (local_now.replace(hour=0, minute=0, second=0).strftime(
#             '%Y-%m-%d %H:%M:%S') , '17時20分'),
#             (local_now.replace(hour=0, minute=0, second=0).strftime(
#             '%Y-%m-%d %H:%M:%S') , '18時20分'),
#             (local_now.replace(hour=0, minute=0, second=0).strftime(
#             '%Y-%m-%d %H:%M:%S') , '19時20分'),
#          )
#
#         self.fields['first_time'].widget.choices = times
#         self.fields['second_time'].widget.choices = times