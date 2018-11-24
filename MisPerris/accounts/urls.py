from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    url(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    url(r'^password-reset/confirm/<uidb64>/<token>$', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    #url(r'^password-reset/done/$', auth_views.PasswordResetDoneView, name="password_reset_done"),
    #url(r'^password-reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)$', auth_views.PasswordResetConfirmView, name="password_reset_confirm"),
    #url(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView, name="password_reset_complete"),
]