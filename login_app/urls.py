from django.urls import path
from . import views

app_name='login_app'

urlpatterns = [
    path('SignUp/', views.sign_up, name='SignUp'),
    path('login/', views.login_page, name='login'),
    path('sign_out/', views.logout_user, name='sign_out'),
    path('profiles/', views.profile, name='profiles'),
    path('edit_profile/', views.user_change, name='edit_profile'),
    path('password/', views.pass_change, name='pass_change'),
    path('add_pic/', views.add_pro_pic, name='add_pic'),
    path('change_pic/', views.change_pro_pic, name='change_pic'),
]