
from django.urls import path,include
from . import views

urlpatterns = [

    path('registration/', views.UserRegistration.as_view(),name="registration"),
    path('login/', views.UserLogin.as_view(),name="login"),
    path('profile/', views.User_Profile_view.as_view(),name="profile"),
    path('changepassword/', views.Change_user_password.as_view(),name="changepassword"),
    path('reset-password-email/', views.ResetPassword_emailview.as_view(),name="resetpasswordemail"),
    path('reset-password/<uid>/<token>/', views.UserPasswordResetView.as_view(),name="resetpassword"),
]
