from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('like_post', views.like_post, name='like_post'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('forgot_password/', auth_views.PasswordResetView.as_view(template_name='forgot_password.html')),
    path('forgot_password/complete/', auth_views.PasswordResetDoneView.as_view(template_name='forgot_password_done.html'), name='password_reset_done'),
    path('forgot_password/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_forgotten_password.html'), name='password_reset_confirm'),
    path('forgot_password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_forgotten_password_done.html'), name='password_reset_complete'),
]