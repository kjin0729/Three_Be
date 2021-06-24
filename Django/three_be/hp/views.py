from django.urls import reverse_lazy
from django.shortcuts import render, redirect, resolve_url
from django.views import generic
from django.views.decorators.http import require_POST
from .models import Blog, Post
from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# Create your views here.


class TopTemplateView(generic.TemplateView):
    template_name = 'hp/top.html'

class BlogListView(generic.ListView):
    model = Blog
    order_by = '-created_at'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'ブログ'
        return context


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'ブログ'
        return context


class PostListView(generic.ListView):
    model = Post
    order_by = '-created_at'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '新着情報'
        return context


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '新着情報'
        return context


class FeeTemplateView(generic.TemplateView):
    template_name = 'hp/fee.html'
    extra_context = {'heading': '料金プラン'}


class IntroduceTemplateView(generic.TemplateView):
    template_name = 'hp/introduce.html'
    extra_context = {'heading': '講師・スタッフの紹介'}


class ContactFormView(generic.FormView):
    template_name = 'hp/contact.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '無料体験レッスンのお申込み'
        return context

    def form_valid(self, form):
        return render(self.request, 'hp/contact.html', {'form': form})


class ContactConfirmView(generic.FormView):
    template_name = 'hp/contact_confirm.html'
    form_class = ContactForm

    def form_valid(self, form):
        return render(self.request, 'hp/contact_confirm.html', {'form': form})

    def form_invalid(self, form):
        return render(self.request, 'hp/contact.html', {'form': form})



# def ContactConfirmView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         user_email = form.cleaned_data.get('email')
#         subject = 'お問い合わせがありました'
#         message = render_to_string('hp/mail/mail.txt', form.cleaned_data, request)
#         from_email = 'alotofmoney07291221@gmail.com'
#         recipient_list = [user_email]
#         bcc = ['alotofmoney07291221@gmail.com']
#         email = EmailMessage(subject, message, from_email, recipient_list, bcc)
#         email.send()
#         return resolve_url('hp:contact_complete')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'hp/contact_confirm.html', context)


class ContactCompleteView(generic.CreateView):
    template_name = 'hp/contact_complete.html'
    form_class = ContactForm
    success_url = reverse_lazy('hp:contact_complete')

    def form_valid(self, form):
        user_email = form.cleaned_data.get('email')
        subject = '【Three Be】お申込みありがとうございます'
        message = render_to_string('hp/mail/mail.txt', form.cleaned_data, self.request)
        from_email = 'alotofmoney07291221@gmail.com'
        recipient_list = [user_email]
        bcc = ['alotofmoney07291221@gmail.com']
        email = EmailMessage(subject, message, from_email, recipient_list, bcc)
        email.send()
        return super().form_valid(form)


    # forms_class = ContactForm
    # success_url = reverse_lazy('hp:contact_confirm')
    #s
    # def form_invalid(self, form):
    #     return render(self.request, 'hp/contact.html', {'form': form})


# class ContactCompleteView(generic.FormView):
#     template_name = 'hp/contact_complete.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('hp:top')
#
#     def form_valid(self, form):

#         return render(self.request, 'hp/contact.complete.html', {'form': form })
#
#     def form_invalid(self, form):
#         return render(self.request, 'hp/contact.html', {'form': form})

# def contact(request):
#     if request.method == 'GET':
#         form = ContactForm(request.session.get('form_data'))
#     else:
#         form = ContactForm(request.POST or None)
#         if form.is_valid():
#             first_date = form.cleaned_data.get('first_date')
#             first_time = form.cleaned_data.get('first_time')
#             second_date = form.cleaned_data.get('second_date')
#             second_time = form.cleaned_data.get('second_date')
#             parent_name = form.cleaned_data.get('parent_name')
#             student_name = form.cleaned_data.get('student_name')
#             birthday = form.cleaned_data.get('birthday')
#             phone_number = form.cleaned_data.get('phone_number')
#             email = form.cleaned_data.get('email')
#             text = form.cleaned_data.get('text')
#             request.session['form_data'] = request.POST
#             return redirect('hp:contact_confirm')
#
#     context = {
#         'form': form,
#         'heading': '無料レッスンのお申込み',
#     }
#
#     return render(request, 'hp/contact.html', context)


# class ContactFormView(generic.FormView):
#     template_name = 'hp/contact.html'
#     form_class = ContactForm
#
#     def form_valid(self, form):
#         first_date = form.cleaned_data.get('first_date')
#         first_time = form.cleaned_data.get('first_time')
#         second_date = form.cleaned_data.get('second_date')
#         second_time = form.cleaned_data.get('second_date')
#         parent_name = form.cleaned_data.get('parent_name')
#         student_name = form.cleaned_data.get('student_name')
#         birthday = form.cleaned_data.get('birthday')
#         phone_number = form.cleaned_data.get('phone_number')
#         email = form.cleaned_data.get('email')
#         text = form.cleaned_data.get('text')
#         return redirect('hp:contact_form')
#
#     context = {
#         'form': form,
#         'heading': '無料レッスンのお申込み',
#     }
#
#         return render(request, 'hp/contact.html', context)

# class ContactFormView(generic.FormView):
#     template_name = 'hp/contact.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('hp:contact_confirm')
#
#     def get_form(self, form_class=None):
#         if 'name' in self.request.POST:
#             form_data = self.request.POST
#         else:
#             form_data = self.request.session.get('form_data', None)
#
#         return self.form_class(form_data)
#
#     def form_valid(self, form):
#         self.request.session['form_data'] = self.request.POST
#         return super().form_valid(form)
#
#
# class ContactConfirmView(generic.TemplateView):
#     template_name = 'hp/contact_confirm.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         form_data = self.request.session.get('form_data', None)
#         context['form'] = ContactForm(form_data)
#         return context

# def contact_confirm(request):
#     session_form_data = request.session.get('form_data')
#     if session_form_data is None:
#         return redirect('hp:contact')
#     else:
#         return redirect('hp:contact_complete')
#
#     context = {
#         'form': ContactForm(session_form_data),
#         'heading': 'お申込み内容の確認',
#     }
#
#     return render(request, 'hp/contact_confirm.html', context)


# def contact_complete(request):
#     session_form_data = request.session.pop('form_data', None)
#     if session_form_data is None:
#         return redirect('hp:contact')
#
#     form = ContactForm(session_form_data)
#     if form.is_valid():
#         form.save()
#         return redirect('hp:top')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'hp/contact.html', context)

