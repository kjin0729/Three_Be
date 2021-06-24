from django.urls import path
from . import views



app_name = 'hp'



urlpatterns = [
    path('', views.TopTemplateView.as_view(), name='top'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('fee/', views.FeeTemplateView.as_view(), name='fee'),
    path('introduce/', views.IntroduceTemplateView.as_view(), name='introduce'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('contact/confirm/', views.ContactConfirmView.as_view(), name='contact_confirm'),
    path('contact/complete/', views.ContactCompleteView.as_view(), name='contact_complete'),
    ]
