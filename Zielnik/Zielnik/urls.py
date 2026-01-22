from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from Users import views as user_views
from Users.forms import UserLoginForm
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [

    path('profile/', user_views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html', authentication_form=UserLoginForm), name='login'),
    path('logout/', user_views.UserLogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='Users/password_reset.html'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Users/password_reset_done.html'), name='password-reset-done'),
    path('', include('Blog.urls')),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Users/password_reset_confirm.html'), name='password-reset-confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Users/password_reset_complete.html'), name='password-reset-complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
